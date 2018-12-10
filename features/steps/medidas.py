'''
Steps para medidas.feature
'''
# pylint: disable=function-redefined
from selenium.webdriver.support.ui import Select
from behave import given, when, then # pylint: disable=no-name-in-module

@given('Vista de agregar medidas')
def step_impl(context):
    '''
    Paso para acceder a vista de medidas nuevas
    '''
    context.browser.get(context.base_url+'/medidas/nuevo')


@when('Mando el form con datos validos de medida')
def step_impl(context):
    '''
    Paso para llenar formulario de medidas
    '''
    inputs_and_values = [
        ('id_nomenclatura', 'nomenclatura medida1'),
        ('id_nombre', 'nombre medida1'),
        ('id_descripcion', 'nombre medida1'),
        ('id_marco_juridico', 'marco medida1'),
        ('id_area', 'area medida1'),
        ('id_nombre_responsable', 'responsable medida1'),
        ('id_apellido_responsable', 'apellido responsable medida1'),
        ('id_nivel_academico_responsable', '1'),
        ('id_ci_responsable', 'V24775895'),
        ('id_impactos-0-descripcion', 'impacto 0 medida1'),
        ('id_objetivos-0-descripcion', 'objetivo 0 medida1'),
        ('id_indicadoresdecumplimientos-0-descripcion', 'indicador 0 medida1')
    ]

    for selector, value in inputs_and_values:
        context.browser.find_element_by_id(selector).send_keys(value)

    Select(context.browser.find_element_by_id('id_tipo')).select_by_visible_text(
        'Correctiva')

    Select(context.browser.find_element_by_id('id_medio')).select_by_visible_text(
        'Socio-Cultural')

    context.browser.find_element_by_id('agregar').click()

@given("La medida agregada aparece en la lista")
@then("La medida agregada aparece en la lista")
def step_impl(context):
    '''
    Paso para verificar que la medida fue agregada
    '''
    assert context.browser.current_url.endswith('/medidas/')

    table = context.browser.find_element_by_tag_name('tbody')
    found = False
    for td in table.find_elements_by_tag_name('td'): # pylint: disable=invalid-name
        if td.text == 'nombre medida1':
            found = True
            break

    assert found


@when('Se quiere editar una medida')
def step_impl(context):
    '''
    Paso para ir a la vista de edicion de medidas
    '''
    context.browser.get(context.base_url+'/medidas/editar/1/')


@when('Edito con datos validos')
def step_impl(context):
    '''
    Paso para mandar datos al form de edicion
    '''
    inputs_and_values = [
        ('id_nomenclatura', 'nomenclatura nueva medida1'),
        ('id_nombre', 'nombre nueva medida1'),
        ('id_descripcion', 'nombre nueva medida1'),
        ('id_marco_juridico', 'marco nueva medida1'),
        ('id_area', 'area nueva medida1'),
        ('id_nombre_responsable', 'responsable nueva medida1'),
        ('id_apellido_responsable', 'apellido responsable nueva medida1'),
        ('id_nivel_academico_responsable', '1'),
        ('id_ci_responsable', 'V24775895'),
        ('id_impactos-0-descripcion', 'impacto 0 nueva medida1'),
        ('id_objetivos-0-descripcion', 'objetivo 0 nueva medida1'),
        ('id_indicadoresdecumplimientos-0-descripcion', 'indicador 0 nueva medida1')
    ]

    for selector, value in inputs_and_values:
        context.browser.find_element_by_id(selector).send_keys(value)

    Select(context.browser.find_element_by_id('id_tipo')).select_by_visible_text(
        'Correctiva')

    Select(context.browser.find_element_by_id('id_medio')).select_by_visible_text(
        'Socio-Cultural')

    context.browser.find_element_by_id('agregar').click()

@given("La medida editada aparece en la lista")
@then("La medida editada aparece en la lista")
def step_impl(context):
    '''
    Paso para verificar que la medida aparece en la lista
    '''
    assert context.browser.current_url.endswith('/medidas/')

    table = context.browser.find_element_by_tag_name('tbody')
    found = False
    for td in table.find_elements_by_tag_name('td'): # pylint: disable=invalid-name
        if td.text == 'nombre nueva medida1':
            found = True
    assert found

@when("Quiero eliminar una medida")
def step_impl(context):
    '''
    Paso para acceder a la vista de eliminacion
    de medidas y eliminar una
    '''
    assert context.browser.current_url.endswith('/medidas/')
    context.browser.get(context.base_url+'/medidas/borrar/1/')
    context.browser.find_element_by_id('id_aceptar').click()
    assert context.browser.current_url.endswith('/medidas/')

@then("La medida no aparece en la lista")
def step_impl(context):
    ''' Paso para verificar que no aparezcan medidas a la base de datos '''
    assert context.browser.current_url.endswith('/medidas/')
    texto_tabla = context.browser.find_element_by_xpath('/html/body/div/main/section/div/p').text
    assert texto_tabla == 'No existen medidas agregadas a la base de datos'
