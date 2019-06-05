// Dependencies
import React, { Component, Redirect } from 'react';
import PropTypes from 'prop-types';
import { Route, Switch } from 'react-router-dom';

// Components
import Login from './User/Login';
import Transfer from './Transfer';
import Password from './User/Password';
import Panel from './Panel';
import Welcome from './Welcome';
import Page404 from './Errors/404';

class ProtectedRoute extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const { component: Component, ...props } = this.props
    return (
      <Route
        {...props}
        render = {props => (
          props.auth ?
            <Component {...props} /> :
            <Redirect to='/login' />
        )}
      />
    )
  }
}

class App extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      authenticated: false,
      userId: ''
    }
  }

  authenticate = (userId=null) => {
    this.setState({ authenticated: !this.state.authenticated, userId: userId});
  }

  render () {
    return (
      <Switch>
        <Route exact path="/" component={() => <Welcome />} />
        <ProtectedRoute exact path="/panel" component={() => <Panel authMethod={this.authenticate} auth={this.state.authenticated} />} />
        <ProtectedRoute exact path="/transfer" component={() => <Transfer authMethod={this.authenticate} auth={this.state.authenticated} />} />
        <Route exact path="/login" component={() => <Login />} />
        <ProtectedRoute exact path="/password" component={() => <Password authMethod={this.authenticate} auth={this.state.authenticated} />} />
        <Route component={() => <Page404 />} />
      </Switch>
    );
  }

}

export default App;
