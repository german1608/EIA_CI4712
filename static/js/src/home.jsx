
// Componente que saluda al usuario la primera vez que se loggea
function Welcome(props) {
    let bienvenida;
    // Condicional que permite dar la bienvenidad si es la primera vez que se loggea
    if (props.proyectoSeleccionado === '') {
        bienvenida = (
            <div className="mensajeEntrada">
                <h1>Bienvenido, {props.nombre}</h1>
                <h2>Selecciona un proyecto</h2>
            </div>
        );
    }
    else {
        bienvenida = <h1>Selecciona un proyecto</h1>;
    };
    return bienvenida;
}

// Clase que maneja la seleccion de proyecto
class SeleccionProyectoForm extends React.Component {

    constructor(props){
        super(props);
        this.state = {value: this.props.nombreProyecto};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    // Maneja el evento en el cual se selecciona un proyecto
    handleChange(event){
        this.setState({value: event.target.value});
    }

    // Maneja el evento cuando se confirma el proyecto
    handleSubmit(event){
        alert('El proyecto seleccionado fue: ' + this.state.value);
    }

    render(){
        const proyectosActuales = this.props.listaProyectos
        const listaProyectos = proyectosActuales.map((proyecto) => 
            <option value={proyecto.pk}>{proyecto.titulo}</option>
        );
        
        return (
            <form onSubmit={this.handleSubmit}>
                <label htmlFor="">
                    <select className="custom-select" value={this.state.value} onChange={this.handleChange}>
                        <option value>Proyecto a editar</option>
                        {listaProyectos}
                    </select>
                </label>
                <input className="btn btn-primary botonSeleccionar" type="submit" value="Elegir"/>
            </form>
        );
    }
}

// Funcion que renderiza toda la aplicacion
function App(props){
    return (
        <div className="seleccionarUnProyecto">
            <Welcome nombre={props.nombreCompleto} proyectoSeleccionado="" />
            <SeleccionProyectoForm nombreProyecto="" listaProyectos={props.contextoProyectos}/>
        </div>
    )
}

// Con ajax se obtiene el json que contiene informacion del back 
// por ejemplo con la lista de proyectos
$.ajax({
    url: "proyectos/",
    type: "GET",
    dataType: "json",
    contentType: "application/json",
    success: function(json){
        // Se obtiene la lista de proyectos asociado
        // al usuario asociado en ese momento
        const listaProyectos = json['proyectos'];
        // Se obtiene del json el usuario que esta 
        // loggeado en el momento
        const usuarioLoggeado = json['usuario'][0];
        ReactDOM.render(
            <App nombreCompleto={usuarioLoggeado['first_name']} contextoProyectos={listaProyectos}/>,
            document.getElementById('seleccionarProyecto')
        ); 
    }
})