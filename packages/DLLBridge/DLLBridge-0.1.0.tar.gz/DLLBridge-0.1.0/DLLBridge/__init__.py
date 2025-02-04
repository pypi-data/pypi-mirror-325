import ctypes
import os

class DLLBridge:
    dll = None  # Variável para armazenar a DLL carregada

    @staticmethod
    def loadDLL(dllnameorpath):
        """
        Carrega uma DLL com base no nome ou caminho fornecido.
        
        :param dllnameorpath: Nome ou caminho da DLL.
        :return: Objeto ctypes que representa a DLL carregada.
        """
        # Verifica se o caminho é válido ou apenas o nome da DLL
        if not os.path.isabs(dllnameorpath):
            # Se for apenas o nome da DLL, tenta carregar diretamente
            dllnameorpath = os.path.join(os.environ.get('SystemRoot', ''), 'System32', dllnameorpath)
            if not os.path.exists(dllnameorpath):
                raise FileNotFoundError(f"DLL não encontrada no sistema: {dllnameorpath}")
        
        try:
            # Carrega a DLL
            DLLBridge.dll = ctypes.CDLL(dllnameorpath)
            print(f"DLL {dllnameorpath} carregada com sucesso.")
            return DLLBridge.dll
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar a DLL: {str(e)}")

    @staticmethod
    def listfunctions(output_file="functions_list.txt"):
        """
        Lista as funções da DLL carregada e as salva em um arquivo de texto.

        :param output_file: Caminho para o arquivo de saída (padrão é "functions_list.txt").
        """
        if DLLBridge.dll is None:
            raise RuntimeError("Nenhuma DLL carregada. Carregue uma DLL primeiro usando loadDLL.")
        
        try:
            # Obtém a lista de funções e métodos da DLL
            functions = dir(DLLBridge.dll)
            with open(output_file, 'w') as f:
                for function in functions:
                    f.write(function + '\n')
            print(f"Funções listadas em {output_file}.")
        except Exception as e:
            raise RuntimeError(f"Erro ao listar funções: {str(e)}")

    @staticmethod
    def usefunction(function_name, parameters=None):
        """
        Chama uma função da DLL carregada com parâmetros fornecidos.

        :param function_name: Nome da função a ser chamada na DLL.
        :param parameters: Lista de parâmetros a serem passados para a função.
        :return: Resultado da chamada da função.
        """
        if DLLBridge.dll is None:
            raise RuntimeError("Nenhuma DLL carregada. Carregue uma DLL primeiro usando loadDLL.")
        
        try:
            # Obtenha a função da DLL
            function = getattr(DLLBridge.dll, function_name)
            if parameters is None:
                parameters = []
            
            # Chama a função com os parâmetros fornecidos
            result = function(*parameters)
            print(f"Função {function_name} chamada com sucesso.")
            return result
        except AttributeError:
            raise ValueError(f"A função '{function_name}' não foi encontrada na DLL.")
        except Exception as e:
            raise RuntimeError(f"Erro ao chamar a função '{function_name}': {str(e)}")



