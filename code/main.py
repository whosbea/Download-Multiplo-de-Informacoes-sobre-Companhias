from abc import ABC
from abc import abstractmethod
from abc import abstractproperty


class User:
    def __init__(self, txtLogin, txtSenha) -> None:
        self._txtLogin = txtLogin
        self._txtSenha = txtSenha

    @classmethod
    def logar(cls, txtLogin, txtSenha):
        return cls(txtLogin, txtSenha)

    @property
    def login(self):
        return self._txtLogin

    @property
    def senha(self):
        return self._txtSenha

    def alterar_senha(self):
        pass


class TipoArquivo:
    def __init__(self, txtDocumento, txtAssuntoIPE) -> None:
        self.txtDocumento = txtDocumento
        self.txtAssuntoIPE = txtAssuntoIPE

    @property
    def txtDocumento(self):
        return self.txtDocumento

    @property
    def txtAssuntoIPE(self):
        return self.txtAssuntoIPE

    def baixar_doc(self):
        pass


class Arquivo():
    def __init__(self, arquivo, txtData, txtHora, email, drive) -> None:
        self.arquivo = arquivo
        self.txtData = txtData
        self.txtHora = txtHora
        self.email = email
        self.drive = drive

    @property
    def arquivo(self):
        return self.arquivo

    @property
    def txtData(self):
        return self.txtData

    @property
    def txtHora(self):
        return self.txtHora

    @property
    def email(self):
        return self.email

    @property
    def drive(self):
        return self.drive

    def enviar_doc(self):
        pass


class Execucoes(ABC):
    @property
    @abstractproperty
    def execucao(self):
        pass

    @abstractmethod
    def registrar_execucao(self):
        pass
    

class AlteracaoSenha(Execucoes):
    def __init__(self, execucao, lista_altecacoes):
        self.execucao = execucao
        self.lista_alteracoes = lista_altecacoes
    
    @property
    def execucao(self):
        return self.execucao
    
    @property
    def lista_alteracoes(self):
        return self.lista_alteracoes
    
    def registrar_alteracao(self):
        pass


class EnvioDoc(Execucoes):
    def __init__(self, execucao, lista_envios) -> None:
        self.execucao = execucao
        self.lista_envios = lista_envios
        
    @property
    def execucao(self):
        return self.execucao
    
    @property
    def lista_envios(self):
        return self.lista_envios
    
    def registrar_execucao(self):
        pass
    

class DownloadDoc(Execucoes):
    def __init__(self, execucao, lista_downloads) -> None:
        self.execucao = execucao
        self.lista_downloads = lista_downloads
    
    @property
    def execucao(self):
        return self.execucao
    
    @property
    def lista_downloads(self):
        return self.lista_downloads
    
    def registrar_execucao(self):
        pass
    
    
        