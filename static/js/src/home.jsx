
// Componente que saluda al usuario la primera vez que se loggea
function Welcome(props) {
    let bienvenida;
    // Condicional que permite dar la bienvenidad si es la primera vez que se loggea
    if (props.proyectoSeleccionado === '') {
        bienvenida = (
            <div className="mensajeEntrada">
                <h1>Bienvenido, {props.nombre}</h1>
                <h2>Seleccionar un proyecto</h2>
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
        const proyectos = ['Proyecto 1', 'Proyecto 2', 'Proyecto 3']
        const listaProyectos = proyectos.map((proyecto) => 
            <option value={proyecto}>{proyecto}</option>
        );
        
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label htmlFor="">
                        <select className="custom-select" value={this.state.value} onChange={this.handleChange}>
                            <option value>Proyecto a editar</option>
                            {listaProyectos}
                        </select>
                    </label>
                    <input className="btn btn-primary botonSeleccionar" type="submit" value="Elegir"/>
                </form>
            </div>
        );
    }
}

// Funcion que renderiza toda la aplicacion
function App(){
    return (
        <div className="seleccionarUnProyecto">
            <Welcome nombre="Daniel" proyectoSeleccionado="" />
            <SeleccionProyectoForm nombreProyecto=""/>
        </div>
    )
}
ReactDOM.render(
    <App />,
    document.getElementById('seleccionarProyecto')
);