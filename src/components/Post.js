import React from 'react'
import { API } from '../manage.js'

class Post extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            post: [],
        }
    }

    componentDidMount() {
        const postid = this.props.match.params.postid
        API.get(`blog/post/${postid}/`)
        .then(res => {
            this.setState({
                post: res.data,
            })
        })
    }

    render() {
        return (
            <div>
                <h1>{ this.state.post.title }</h1>
                <p>{ this.state.post.content }</p>
            </div>
        )
    }
}

export default Post