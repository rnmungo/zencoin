import React, { Component } from 'react';
import {Link} from 'react-router-dom';
import '../Global/css/bootstrap.min.css';
import '../Global/css/Login.css';
import axios from 'axios';


class Register extends Component {

    constructor(props) {
        super(props);
        this.state = {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            message: ''
        }
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleButtonClick = this.handleButtonClick.bind(this);
    }

    handleInputChange(e) {
        if(e.target.id === 'first_name') {
            this.setState({first_name: e.target.value});
        }
        else if(e.target.id === 'last_name') {
            this.setState({last_name: e.target.value});
        }
        else if(e.target.id === 'email') {
            this.setState({email: e.target.value});
        }
        else if(e.target.id === 'password') {
            this.setState({password: e.target.value});
        }
    }

    handleButtonClick() {
        const instance = axios.create({ baseURL: 'http://localhost:9000' });
        instance.post('/users', {
            'first_name': this.state.first_name,
            'last_name': this.state.last_name,
            'email': this.state.email,
            'password': this.state.password,
            'role': 'customer'
        }).then((res) => {
          if (res.status === 200) {
            this.setState({
                message: '¡Usuario registrado correctamente!',
                first_name: '',
                last_name: '',
                email: '',
                password: ''});
          }
        }).catch((err) => {
            this.setState({
                message: '¡Error al enviar la solicitud de registro!',
            });
        });
    }

    render () {
      return (
        <div className="text-center Content">
            <div className="container">
                <h3>Registro</h3>
                <div className="form-group row text-left mt-3 justify-content-center">
                    <div className="col-12 col-md-6">
                        <input id="first_name" type="text" className="form-control form-control-sm shadow-sm mt-1" value={this.state.first_name} onChange={this.handleInputChange} aria-describedby="fNameHelp" />
                        <small id="fNameHelp" className="form-text">Nombre</small>
                    </div>
                </div>
                <div className="form-group row text-left mt-3 justify-content-center">
                    <div className="col-12 col-md-6">
                        <input id="last_name" type="text" className="form-control form-control-sm shadow-sm mt-1" value={this.state.last_name} onChange={this.handleInputChange} aria-describedby="lNameHelp" />
                        <small id="lNameHelp" className="form-text">Apellido</small>
                    </div>
                </div>
                <div className="form-group row text-left mt-3 justify-content-center">
                    <div className="col-12 col-md-6">
                        <input id="email" type="text" className="form-control form-control-sm shadow-sm mt-1" value={this.state.email} onChange={this.handleInputChange} aria-describedby="emailHelp" />
                        <small id="emailHelp" className="form-text">E-Mail</small>
                    </div>
                </div>
                <div className="form-group row text-left mt-3 justify-content-center">
                    <div className="col-12 col-md-6">
                        <input id="password" type="password" className="form-control form-control-sm shadow-sm mt-1" value={this.state.password} onChange={this.handleInputChange} aria-describedby="passwordHelp" />
                        <small id="passwordHelp" className="form-text">Contraseña</small>
                    </div>
                </div>
                <button type="button" className="btn btn-success shadow-sm mx-2" onClick={this.handleButtonClick}>Confirmar</button>
                <Link className="btn btn-secondary shadow-sm" to="/">Volver al Inicio</Link>
                <p>{this.state.message}</p>
            </div>
        </div>
      );
    }
}

export default Register;
