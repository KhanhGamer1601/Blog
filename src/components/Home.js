import React from 'react'
import { API } from '../manage.js'
import { Link } from 'react-router-dom'

class Home extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            posts: [],
        }
    }

    componentDidMount() {
        API.get('blog/post/')
        .then(res => {
            this.setState({
                posts: res.data
            })
        })
    }

    render() {
        return (
            <div>
                <div>
                    {
                        this.state.posts.map(post => (
                            <h3 id={ post.id }><Link to={ `/post/${post.id}/` }>{ post.title }</Link></h3>
                        ))
                    }
                </div>
            </div>
        )
    }
}

export default Home