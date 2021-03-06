import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')

from instruccion import *
from Lista import *
from TablaSimbolos import *

class Use(Instruccion):

    def __init__(self, dbid):
        self.dbid = dbid

    def execute(self, data):
        if data.comprobarExistencia(self.dbid.column.upper(), 'database'):
            data.databaseSeleccionada = self.dbid.column.upper()
            return 'La base de datos ' + data.databaseSeleccionada + ' ha sido seleccionada.'
        else:
            return 'No existe la base de datos.'

    def __repr__(self):
        return str(self.__dict__)
