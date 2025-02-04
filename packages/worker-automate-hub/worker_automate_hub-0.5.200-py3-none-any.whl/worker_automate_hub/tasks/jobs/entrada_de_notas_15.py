import asyncio
import getpass
import os
import warnings

import pyautogui
from pywinauto.keyboard import send_keys
from PIL import Image, ImageEnhance
import pytesseract
from pywinauto.application import Application
from pywinauto_recorder.player import set_combobox
from rich.console import Console

from worker_automate_hub.api.ahead_service import save_xml_to_downloads
from worker_automate_hub.api.client import (
    get_config_by_name,
    get_status_nf_emsys,
    sync_get_config_by_name,
)
from worker_automate_hub.config.settings import load_env_config
from worker_automate_hub.models.dto.rpa_historico_request_dto import (
    RpaHistoricoStatusEnum,
    RpaRetornoProcessoDTO,
    RpaTagDTO,
    RpaTagEnum,
)
from worker_automate_hub.models.dto.rpa_processo_entrada_dto import (
    RpaProcessoEntradaDTO,
)
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import (
    check_nota_importada,
    error_after_xml_imported,
    error_before_persist_record,
    import_nfe,
    is_window_open,
    is_window_open_by_class,
    itens_not_found_supplier,
    kill_process,
    login_emsys,
    set_variable,
    type_text_into_field,
    verify_nf_incuded,
    warnings_after_xml_imported,
    worker_sleep,
)
from worker_automate_hub.utils.utils_nfe_entrada import EMSys

pyautogui.PAUSE = 0.5
console = Console()

emsys = EMSys()


async def entrada_de_notas_15(task: RpaProcessoEntradaDTO) -> RpaRetornoProcessoDTO:
    """
    Processo que relazia entrada de notas no ERP EMSys(Linx).

    """
    try:
        # Get config from BOF
        config = await get_config_by_name("login_emsys")
        console.print(task)

        console.print(config)

        # Seta config entrada na var nota para melhor entendimento
        nota = task.configEntrada
        multiplicador_timeout = int(float(task.sistemas[0].timeout))
        set_variable("timeout_multiplicador", multiplicador_timeout)

        # Abre um novo emsys
        await kill_process("EMSys")

        #Verifica se a nota ja foi lançada
        console.print("\nVerifica se a nota ja foi lançada...")
        nf_chave_acesso = int(nota.get("nfe"))
        status_nf_emsys = await get_status_nf_emsys(nf_chave_acesso)
        if status_nf_emsys.get("status") == "Lançada":
            console.print("\nNota ja lançada, processo finalizado...", style="bold green")
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno="Nota já lançada",
                status=RpaHistoricoStatusEnum.Descartado,
            )
        else:
            console.print("\nNota não lançada, iniciando o processo...")

        app = Application(backend="win32").start("C:\\Rezende\\EMSys3\\EMSys3.exe")
        warnings.filterwarnings(
            "ignore",
            category=UserWarning,
            message="32-bit application should be automated using 32-bit Python",
        )
        console.print("\nEMSys iniciando...", style="bold green")
        return_login = await login_emsys(config.conConfiguracao, app, task)

        if return_login.sucesso == True:
            type_text_into_field(
                "Nota Fiscal de Entrada", app["TFrmMenuPrincipal"]["Edit"], True, "50"
            )
            pyautogui.press("enter")
            await worker_sleep(1)
            pyautogui.press("enter")
            console.print(
                f"\nPesquisa: 'Nota Fiscal de Entrada' realizada com sucesso",
                style="bold green",
            )
        else:
            logger.info(f"\nError Message: {return_login.retorno}")
            console.print(f"\nError Message: {return_login.retorno}", style="bold red")
            return return_login

        await worker_sleep(10)

        # Procura campo documento
        console.print("Navegando pela Janela de Nota Fiscal de Entrada...\n")
        app = Application().connect(title="Nota Fiscal de Entrada")
        main_window = app["Nota Fiscal de Entrada"]

        console.print(
            "Controles encontrados na janela 'Nota Fiscal de Entrada', navegando entre eles...\n"
        )
        panel_TNotebook = main_window.child_window(
            class_name="TNotebook", found_index=0
        )
        panel_TPage = panel_TNotebook.child_window(class_name="TPage", found_index=0)
        panel_TPageControl = panel_TPage.child_window(
            class_name="TPageControl", found_index=0
        )
        panel_TTabSheet = panel_TPageControl.child_window(
            class_name="TTabSheet", found_index=0
        )
        combo_box_tipo_documento = panel_TTabSheet.child_window(
            class_name="TDBIComboBox", found_index=1
        )

        combo_box_tipo_documento.click()
        console.print(
            "Clique select box, Tipo de documento realizado com sucesso, selecionando o tipo de documento...\n"
        )

        await worker_sleep(4)

        set_combobox("||List", "NOTA FISCAL DE ENTRADA ELETRONICA - DANFE")
        console.print(
            "Tipo de documento 'NOTA FISCAL DE ENTRADA ELETRONICA - DANFE', selecionado com sucesso...\n"
        )

        await worker_sleep(4)

        # Clica em 'Importar-Nfe'
        imported_nfe = await import_nfe()
        if imported_nfe.sucesso == True:
            console.log(imported_nfe.retorno, style="bold green")
        else:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=imported_nfe.retorno,
                status=RpaHistoricoStatusEnum.Falha,
                tags=[RpaTagDTO(descricao=RpaTagEnum.Tecnico)]
            )

        await worker_sleep(10)

        # Download XML
        await save_xml_to_downloads(nota["nfe"])

        # Permanece 'XML'
        # Clica em  'OK' para selecionar
        pyautogui.click(970, 666)
        await worker_sleep(3)

        # Click Downloads
        await emsys.get_xml(nota["nfe"])
        await worker_sleep(15)

        # VERIFICANDO A EXISTENCIA DE WARNINGS
        warning_pop_up = await is_window_open("Warning")
        if warning_pop_up["IsOpened"] == True:
            warning_work = await warnings_after_xml_imported()
            if warning_work.sucesso == True:
                console.log(warning_work.retorno, style="bold green")
            else:
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=warning_work.retorno,
                    status=RpaHistoricoStatusEnum.Falha,
                    tags=[RpaTagDTO(descricao=RpaTagEnum.Tecnico)]
                )

        # VERIFICANDO A EXISTENCIA DE ERRO
        erro_pop_up = await is_window_open("Erro")
        if erro_pop_up["IsOpened"] == True:
            error_work = await error_after_xml_imported()
            return RpaRetornoProcessoDTO(
                sucesso=error_work.sucesso,
                retorno=error_work.retorno,
                status=error_work.status,
                tags=error_work.tags
            )

        # Deleta o xml
        await emsys.delete_xml(nota.get("nfe"))
        await worker_sleep(5)

        app = Application().connect(
            title="Informações para importação da Nota Fiscal Eletrônica"
        )
        main_window = app["Informações para importação da Nota Fiscal Eletrônica"]

        # INTERAGINDO COM A DATA DE ENTRADA
        await worker_sleep(2)
        try:
            recebimento_fisico = nota.get("recebimentoFisico", None)
            if recebimento_fisico:
                recebimento_fisico = nota["recebimentoFisico"].split(" ")
                pyautogui.write(recebimento_fisico[0])
                await worker_sleep(2)
        except:
            console.print(
                f"A chave recebimentoFisico não está presente na config de entrada...\n"
            )


        combo_box_natureza_operacao = main_window.child_window(
            class_name="TDBIComboBox", found_index=0
        )
        combo_box_natureza_operacao.click()
        await worker_sleep(4)
        set_combobox("||List", "1652-COMPRA DE MERCADORIAS- 1.652")
        await worker_sleep(3)

        # INTERAGINDO COM O CAMPO ALMOXARIFADO
        filial_empresa_origem = nota.get("filialEmpresaOrigem")
        valor_almoxarifado = filial_empresa_origem + "50"
        pyautogui.press("tab")
        pyautogui.write(valor_almoxarifado)
        await worker_sleep(2)
        pyautogui.press("tab")

        await worker_sleep(10)
        console.print("Clicando em OK... \n")

        max_attempts = 3
        i = 0
        while i < max_attempts:
            console.print("Clicando no botão de OK...\n")
            try:
                try:
                    btn_ok = main_window.child_window(title="Ok")
                    btn_ok.click()
                except:
                    btn_ok = main_window.child_window(title="&Ok")
                    btn_ok.click()
            except:
                console.print("Não foi possivel clicar no Botão OK... \n")

            await worker_sleep(1)
            i += 1
        
        await worker_sleep(2)

        try:
            console.print("Verificando itens não localizados ou NCM...\n")
            itens_by_supplier = await is_window_open_by_class("TFrmAguarde", "TMessageForm")

            if itens_by_supplier["IsOpened"] == True:
                itens_by_supplier_work = await itens_not_found_supplier(nota.get("nfe"))

                if not itens_by_supplier_work.sucesso:
                    return itens_by_supplier_work

        except Exception as error:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=f"Falha ao verificar a existência de POP-UP de itens não localizados: {error}",
                status=RpaHistoricoStatusEnum.Falha,
                tags=[RpaTagDTO(descricao=RpaTagEnum.Tecnico)]
            )

        await worker_sleep(3)

        console.print("Navegando pela Janela de Nota Fiscal de Entrada...\n")
        app = Application().connect(class_name="TFrmNotaFiscalEntrada")
        main_window = app["TFrmNotaFiscalEntrada"]

        main_window.set_focus()

        await emsys.verify_warning_and_error("Information", "&No")

        await worker_sleep(10)
        console.print("Navegando pela Janela de Nota Fiscal de Entrada...\n")
        app = Application().connect(class_name="TFrmNotaFiscalEntrada")
        main_window = app["TFrmNotaFiscalEntrada"]

        main_window.set_focus()
        console.print("Acessando a aba de Pagamentos... \n")
        panel_TPage = main_window.child_window(class_name="TPage", title="Formulario")
        panel_TTabSheet = panel_TPage.child_window(class_name="TcxCustomInnerTreeView")
        panel_TTabSheet.wait("visible")
        panel_TTabSheet.click()
        send_keys("{DOWN " + ("7") + "}")

        panel_TPage = main_window.child_window(class_name="TPage", title="Formulario")
        panel_TTabSheet = panel_TPage.child_window(class_name="TPageControl")

        panel_TabPagamento = panel_TTabSheet.child_window(class_name="TTabSheet")

        panel_TabPagamentoCaixa = panel_TTabSheet.child_window(title="Pagamento Pelo Caixa")

        tipo_cobranca = panel_TabPagamentoCaixa.child_window(
            class_name="TDBIComboBox", found_index=0
        )

        console.print(f"Selecionando a Especie de Caixa... \n")
        tipo_cobranca.click()
        try:
            set_combobox("||List", "BANCO DO BRASIL BOLETO")
        except:
            set_combobox("||List", "BOLETO")
        
        await emsys.inserir_vencimento_e_valor(
            nota.get("nomeFornecedor"),
            nota.get("dataEmissao"),
            nota.get("dataVencimento"),
            nota.get("valorNota"),
        )
        await worker_sleep(8)
        await emsys.incluir_registro()
        await worker_sleep(5)

        await emsys.verify_warning_and_error("Warning", "No")
        await emsys.verify_warning_and_error("Warning", "&No")

        try:
            erro_pop_up = await is_window_open("Information")
            if erro_pop_up["IsOpened"] == True:
                error_work = await error_before_persist_record()
                return RpaRetornoProcessoDTO(
                    sucesso=error_work.sucesso,
                    retorno=error_work.retorno,
                    status=error_work.status,
                )
        except:
            console.print("Erros não foram encontrados após incluir o registro")

        max_attempts = 60
        i = 0

        while i < max_attempts:
            information_pop_up = await is_window_open("Information")
            if information_pop_up["IsOpened"] == True:
                # Verifica se a info 'Nota fiscal incluida' está na tela
                try:
                    app = Application().connect(class_name="TFrmNotaFiscalEntrada")
                    main_window = app["Information"]

                    main_window.set_focus()

                    console.print(f"Tentando clicar no Botão OK...\n")
                    btn_ok = main_window.child_window(class_name="TButton")

                    if btn_ok.exists():
                        btn_ok.click()
                        break
                    else:
                        console.print(f" botão OK Não enontrado")
                except Exception as e:
                    try:
                        await worker_sleep(5)
                        await emsys.verify_warning_and_error("Warning", "OK")
                        await emsys.verify_warning_and_error("Aviso", "OK")
                        alterar_nop = await emsys.alterar_nop(nota["cfop"], nota["nfe"])

                        if alterar_nop:
                            return alterar_nop
                    except Exception as error:
                        observacao = f"Erro Processo Entrada de Notas: {str(error)}"
                        logger.error(observacao)
                        console.print(observacao, style="bold red")
                        return RpaRetornoProcessoDTO(
                            sucesso=False,
                            retorno=observacao,
                            status=RpaHistoricoStatusEnum.Falha,
                            tags=[RpaTagDTO(descricao=RpaTagEnum.Tecnico)]
                        )
            else:
                console.print(f"Aguardando confirmação de nota incluida...\n")
                await worker_sleep(5)
                i += 1
        
        await worker_sleep(15)
        console.print("\nVerifica se a nota ja foi lançada...")
        nf_chave_acesso = int(nota.get("nfe"))
        status_nf_emsys = await get_status_nf_emsys(nf_chave_acesso)
        if status_nf_emsys.get("status") != "Lançada":
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=f"Erro ao lançar nota",
                status=RpaHistoricoStatusEnum.Descartado,
            )
        else:
            nf_imported = await check_nota_importada(nota.get("nfe"))
            if nf_imported.sucesso == True:
                await worker_sleep(12)
                console.print("\nVerifica se a nota ja foi lançada...")
                status_nf_emsys = await get_status_nf_emsys(nf_chave_acesso)
                if status_nf_emsys.get("status") == "Lançada":
                    console.print("\nNota lançada com sucesso, processo finalizado...", style="bold green")
                    return RpaRetornoProcessoDTO(
                        sucesso=True,
                        retorno="Nota Lançada com sucesso!",
                        status=RpaHistoricoStatusEnum.Sucesso,
                    )
                else:
                    console.print("Erro ao lançar nota", style="bold red")
                    return RpaRetornoProcessoDTO(
                        sucesso=False,
                        retorno=f"Pop-up nota incluida encontrada, porém nota encontrada como 'já lançada' trazendo as seguintes informações: {nf_imported.retorno} - {error_work}",
                        status=RpaHistoricoStatusEnum.Falha,
                        tags=[RpaTagDTO(descricao=RpaTagEnum.Negocio)]
                    )
            else:
                console.print("Erro ao lançar nota", style="bold red")
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=f"Erro ao lançar nota, erro: {nf_imported.retorno}",
                    status=RpaHistoricoStatusEnum.Falha,
                    tags=[RpaTagDTO(descricao=RpaTagEnum.Tecnico)]
                )
    
    except Exception as ex:
        observacao = f"Erro Processo Entrada de Notas: {str(ex)}"
        logger.error(observacao)
        console.print(observacao, style="bold red")
        return RpaRetornoProcessoDTO(
            sucesso=False,
            retorno=observacao,
            status=RpaHistoricoStatusEnum.Falha,
            tags=[RpaTagDTO(descricao=RpaTagEnum.Tecnico)]
        )
