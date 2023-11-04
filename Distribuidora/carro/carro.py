class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro']={}
        
        self.carro = carro
            
#------------------------------------------------------------------

    def agregar(self, productos):
        if(str(productos.id) not in self.carro.keys()):
            self.carro[productos.id] = {
                "productos_id" : productos.id,
                "nombre" : productos.nombre_producto,
                "precio" : str(productos.precio),
                "cantidad" : 1,
                "imagen" : productos.imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(productos.id):
                    value ['cantidad'] = value ['cantidad']+1
                    value['precio']=float(value['precio'])+productos.precio
                    break

        self.guardar_carro()

#------------------------------------------------------------------

    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True

#------------------------------------------------------------------

    def eliminar(self, productos):
        productos.id = str(productos.id)
        if productos.id in self.carro:
            del self.carro[productos.id]
            self.guardar_carro()

#------------------------------------------------------------------

    def restar_producto(self, productos):
        for key, value in self.carro.items():
            if key == str(productos.id):
                value ['cantidad'] = value ['cantidad'] - 1
                value['precio']=float(value['precio'])-productos.precio
                if  value ['cantidad'] < 1:
                    self.eliminar(productos)
                break
        self.guardar_carro()

#------------------------------------------------------------------

    def limpiar_carro(self):
        self.session['carro']={}
        self.session.modified = True