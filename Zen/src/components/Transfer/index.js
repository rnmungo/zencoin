import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Navbar from '../Panel/Navbar';
import TransferContent from './TransferContent';
import axios from  'axios';


class Transfer extends Component {

    constructor(props) {
      super(props);
      this.state = {
        account: {}
      }
    }

    static propTypes = {
        user: PropTypes.object.isRequired
    }

    componentDidMount() {
      if (this.props.user.id) {
        const instance = axios.create({ baseURL: 'http://localhost:9000' });
        instance.get('/accounts/' + this.props.user.id)
          .then((res) => {
            if (res.status === 200) {
              this.setState({account: res.data})
            }
        }).catch((err) => {
          console.log(err);
        });
      }
    }

    render () {
      const { user } = this.props;
      return (
        <div>
          <Navbar username={user.first_name + ' ' + user.last_name} handleLogOut={this.props.handleLogOut} />
          <TransferContent account={this.state.account} />
        </div>
      );
    }
}

export default Transfer;
