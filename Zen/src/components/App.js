// Dependencies
import React, { Component } from 'react';
import createHashHistory from 'history/createBrowserHistory'
import { Route, Switch } from 'react-router-dom';

// Components
import Login from './User/Login';
import Transfer from './Transfer';
import Register from './User/Register';
import Panel from './Panel';
import Welcome from './Welcome';
import Page404 from './Errors/404';
import axios from  'axios';


class App extends Component {

  constructor(props) {
    super(props);
    let userId = '';
    let authenticated = false;
    if (typeof(Storage) !== 'undefined') {
      userId = localStorage.getItem('ZenCoinUserId');
      authenticated = (localStorage.getItem('ZenCoinAuthenticated') === 'true');
    }
    this.state = {
      authenticated: authenticated,
      userId: userId,
      user: {}
    }
  }

  componentDidMount() {
    if (this.state.authenticated && this.state.userId) {
      const instance = axios.create({ baseURL: 'http://localhost:9000' });
      instance.get('/users/' + this.state.userId)
        .then((res) => {
          if (res.status === 200) {
            this.setState({user: res.data});
          }
        }).catch((err) => {
          console.log(err)
      });
    }
  }

  authenticate = (userId=null) => {
    if (typeof(Storage) !== 'undefined') {
      localStorage.setItem('ZenCoinUserId', userId);
      localStorage.setItem('ZenCoinAuthenticated', userId ? true : false);
    }
    this.setState({
      authenticated: !this.state.authenticated,
      userId: userId
    }, () => this.redirectToPage('/panel'));
  }

  redirectToPage = (url) => {
    let history = createHashHistory();
    history.push(url);
    window.location.reload();
  }

  logOut = () => {
    localStorage.removeItem('ZenCoinUserId');
    localStorage.removeItem('ZenCoinAuthenticated');
    this.setState({
      authenticated: !this.state.authenticated,
      userId: ''
    }, () => this.redirectToPage('/login'));
  }

  render () {
      return (
        <Switch>
          <Route exact path="/" component={() => <Welcome auth={this.state.authenticated} />} />
          <Route exact path="/login" component={() => <Login authMethod={this.authenticate} />} />
          <Route exact path="/register" component={() => <Register />} />
          <Route
            exact
            path="/panel"
            component={
              () => this.state.authenticated
                ? <Panel user={this.state.user} handleLogOut={this.logOut} />
                : <Login authMethod={this.authenticate} />
              } />
          <Route
            exact
            path="/transfer"
            component={
              () => this.state.authenticated
                ? <Transfer user={this.state.user} handleLogOut={this.logOut} />
                : <Login authMethod={this.authenticate} />
              } />
          <Route component={() => <Page404 />} />
        </Switch>
      );
  }
}

export default App;
