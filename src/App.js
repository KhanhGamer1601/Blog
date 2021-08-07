import React from 'react'
import { BrowserRouter as Router, Link } from 'react-router-dom'
import BaseRouter from './manage.js'
import './App.css'

class App extends React.Component {
  render() {
    return (
      <Router>
        <div className="App">
          <nav>
            <ul>
              <li><Link to="/">Home</Link></li>
            </ul>
          </nav>
          <BaseRouter></BaseRouter>
        </div>
      </Router>
    )
  }
}

export default App