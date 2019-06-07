import React, { Component } from 'react';
import PropTypes from 'prop-types';
import '../Global/css/bootstrap.min.css';
import Account from './Account';
import Cotization from './Cotization';
import Transfers from './Transfers';
import axios from  'axios';


class Charts extends Component {

    constructor(props) {
      super(props);
      this.state = {
        account: {},
        conversions: [],
        transfers: []
      }
    }

    static propTypes = {
        user: PropTypes.object.isRequired
    }

    getTransfers = (account) => {
      const instance = axios.create({ baseURL: 'http://localhost:9000' });
      instance.get('/movements/' + account.id)
        .then((res) => {
          if (res.status === 200) {
            this.setState({transfers: res.data});
          }
      }).catch((err) => {
        console.log(err);
      });
    }

    getConversions = (account) => {
      if (account.id) {
        const instance = axios.create({ baseURL: 'http://localhost:9000' });
        instance.get('/conversions/' + account.currency.id)
          .then((res) => {
            if (res.status === 200) {
              this.setState({conversions: res.data});
            }
        }).catch((err) => {
          console.log(err);
        });
      }
    }

    getAssociatedData = (account) => {
      this.getConversions(account);
      this.getTransfers(account);
    }

    componentDidMount() {
      if (this.props.user.id) {
        const instance = axios.create({ baseURL: 'http://localhost:9000' });
        instance.get('/accounts/' + this.props.user.id)
          .then((res) => {
            if (res.status === 200) {
              this.setState({account: res.data}, () => this.getAssociatedData(this.state.account));
            }
        }).catch((err) => {
          console.log(err);
        });
      }
    }

    render () {
      return (
        <div className="container mt-5">
          <div className="row justify-content-center">
            <div className="col-12 col-md-5">
              <Account account={this.state.account}/>
              <Cotization conversions={this.state.conversions} />
            </div>
            <div className="col-12 col-md-7">
              <Transfers transfers={this.state.transfers} accountId={this.state.account.id}/>
            </div>
          </div>
        </div>
      );
    }
}

export default Charts;
