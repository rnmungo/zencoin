import React, { Component } from 'react';
import PropTypes from 'prop-types';
import '../Global/css/bootstrap.min.css';
import axios from 'axios';


class TransferContent extends Component {

    constructor(props) {
      super(props);
      this.state = {
        number: 0,
        amount: 0,
        error: ''
      }
      this.handleInputChange = this.handleInputChange.bind(this);
      this.handleButtonClick = this.handleButtonClick.bind(this);
    }

    static propTypes = {
        account: PropTypes.object.isRequired
    }

    transfer = (to_account) => {
      const instance = axios.create({ baseURL: 'http://localhost:9000' });
      instance.post('/transfers', {
        'from_account_id': this.props.account.id,
        'to_account_id': to_account.id,
        'total': this.state.amount
      }).then((res) => {
          if (res.status === 200) {
            this.props.account.saldo -= this.state.amount;
            this.setState({message: 'Transferencia realizada con éxito!'});
          }
      }).catch((err) => {
        this.setState({
          message: '¡Error al realizar la transferencia!',
        });
      });
    }

    handleButtonClick() {
      if (this.state.number <= 0 || this.state.amount <= 0) {
        this.setState({message: 'Error de datos, complete el formulario correctamente.'})
      }
      else {
        const instance = axios.create({ baseURL: 'http://localhost:9000' });
        instance.get('/destiny/' + this.state.number)
          .then((res) => {
            if (res.status === 200) {
              this.transfer(res.data);
            }
        }).catch((err) => {
          this.setState({
            message: '¡El número de cuenta de destino no es válido!',
          });
        });
      }
    }

    handleInputChange(e) {
      if (e.target.id === "amount") {
        this.setState({amount: Number(e.target.value)})
      }
      else if (e.target.id === "accountNumber") {
        this.setState({number: Number(e.target.value)})
      }
    }

    render () {
      const { account } = this.props;
      return (
        <div className="container text-center mt-5">
          <h3>Transferencia Inmediata</h3>
          <h2>Saldo Actual {Math.round(account.saldo, 5)} ZenCoins</h2>
          <div className="form-group row text-left mt-5">
            <div className="col-12 col-sm-6 col-lg-12 col-xl-6">
              <input id="accountNumber" type="number" className="form-control form-control-sm shadow-sm mt-1" value={this.state.number} onChange={this.handleInputChange} aria-describedby="accountNumberHelp" />
              <small id="accountNumberHelp" className="form-text text-muted">Número de Cuenta del Destinatario</small>
            </div>
            <div className="col-12 col-sm-6 col-lg-12 col-xl-6">
              <input id="amount" type="number" className="form-control form-control-sm shadow-sm mt-1" value={this.state.amount} onChange={this.handleInputChange} aria-describedby="amountHelp" />
              <small id="amountHelp" className="form-text text-muted">Monto a Transferir</small>
            </div>
          </div>
          <button type="button" className="btn btn-sm btn-success" onClick={this.handleButtonClick}>Transferir</button>
          <p>{this.state.message}</p>
        </div>
      );
    }
}

export default TransferContent;
