from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    #Cantidad de registros que se mostraran por pagina
    page_size = 5  
    # Permite modificar el tamaño por query param
    page_size_query_param = "page_size" 
    #Cantidad de resgistros maximos por pagina
    max_page_size = 100 
