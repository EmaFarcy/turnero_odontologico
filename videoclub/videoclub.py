import pickle #libreria para guardar y recuperar informacion
from abb import ArbolBinarioBusqueda

class Socio():
    def __init__(self,dni,nombre,telefono,domicilio):
        self.dni =dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
        
    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.dni<other.dni
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.dni<=other.dni
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.dni==other.dni
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.dni!=other.dni
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.dni>other.dni
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.dni>=other.dni

    def __str__(self):
        return "DNI: {0}\nNombre: {1}\nTelefono: {2}\nDomicilio: {3}\n" \
            .format(self.dni,self.nombre,self.telefono,self.domicilio)

class Pelicula():
    def __init__(self,titulo,genero,anio):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.alquilada = None
    
    def __str__(self):
        return "Titulo: {0}\nGenero: {1}\nAño: {2}\nAlquilada: {3}" \
            .format(self.titulo,self.genero,self.anio,self.alquilada)
        #return f"Titulo: {self.titulo}\nGenero: {self.genero}\nAño: {self.anio}\nAlquilada: {self.alquilada}"

    def esta_alquilada(self):
        return self.alquilada != None
    
    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.titulo<other.titulo
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.titulo<=other.titulo
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.titulo==other.titulo
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.titulo!=other.titulo
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.titulo>other.titulo
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.titulo>=other.titulo

class Videoclub:
    def __init__(self):
        self.socios = ArbolBinarioBusqueda() #ABB de socios (clientes)
        self.peliculas = ArbolBinarioBusqueda() #ABB de peliculas
    def contiene_socio(self,dni)->bool:
        esta = False
        for socio in self.socios:
            if socio.dni == dni:
                esta = True
        return esta
    def buscar_socio(self,dni)->bool:
        devolver = None
        for socio in self.socios:
            if socio.dni == dni:
                devolver = socio
        return devolver
    def alta_nuevo_socio(self,socio):
        self.socios.append(socio)
        
    def baja_socio(self,dni):
        socio = self.buscar_socio(dni)
        self.socios.remove(socio)
    
    def mostrar_socios(self):
        for socio in self.socios:
            print (socio)
    
    def contiene_pelicula(self,titulo):
        return self.peliculas.__contains__(titulo) #devuelve true o false. Usamos el metodo __contains__ del ABB
    
    def buscar_pelicula(self,titulo)->"Pelicula":
        return self.peliculas.__getitem__(titulo) #devuelve la pelicula. Usamos el metodo __getitem__ del ABB
    
        
    def alta_nueva_pelicula(self,pelicula)->None:
        if not self.contiene_pelicula(pelicula.titulo):
            self.peliculas.append(pelicula) #agregamos por título la pelicula al ABB de peliculas
        
        
    def baja_pelicula(self,titulo, dni)->None:
        pelicula = self.buscar_pelicula(titulo)
        if pelicula and not pelicula.esta_alquilada(): #si la pelicula existe y no esta alquilada. 
            pelicula.alquilada = dni
        
    def alquilar_pelicula(self,titulo,dni):
        pelicula = self.buscar_pelicula(titulo)
        if pelicula and pelicula.esta_alquilada() is None:
            pelicula.alquilada = dni #Alquilamos la pelicula
                
    def devolver_pelicula(self,titulo):
        pelicula = self.buscar_pelicula(titulo)
        if pelicula and pelicula.esta_alquilada() is not None:
            pelicula.alquilada = None #Marcamos como devuelta la pelicula
         
    def guardar_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo, 'wb')
        pickle.dump(self, pickle_file)
        pickle_file.close()

    def leer_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo,'rb')
        video = pickle.load(pickle_file)
        self.socios = video.socios
        self.peliculas = video.peliculas
        pickle_file.close()

