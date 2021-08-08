import axios from 'axios'
import { Route } from 'react-router-dom'
import Home from './components/Home.js'
import Post from './components/Post.js'

export const API = axios.create({
    baseURL: 'http://localhost:16/',
})

function BaseRouter() {
    return (
        <div>
            <Route path="/" exact component={ Home }></Route>
            <Route path="/post/:postid/" exact component={ Post }></Route>
        </div>
    )
}

export default BaseRouter