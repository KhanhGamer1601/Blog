import axios from 'axios'
import { Route } from 'react-router-dom'
import Home from './components/Home.js'

const API = axios.create({
    baseURL: 'http://localhost:16/',
})

function BaseRouter() {
    return (
        <div>
            <Route path="/" exact component={ Home }></Route>
        </div>
    )
}

export default API
export default BaseRouter