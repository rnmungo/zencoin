import React, { Component } from 'react';
import PropTypes from 'prop-types';
import '../Global/css/Login.css';
import Navbar from './Navbar';
import Charts from './Charts';


class Panel extends Component {

    static propTypes = {
        user: PropTypes.object.isRequired
    }

    render () {
      const { user } = this.props;
      return (
        <div>
          <Navbar username={user.first_name + ' ' + user.last_name} handleLogOut={this.props.handleLogOut} />
          <Charts user={user} />
        </div>
      );
    }
}

export default Panel;
