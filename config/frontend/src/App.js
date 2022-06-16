import React, { Component } from 'react';
import axios from 'axios'; // new
const list = [
    {
        "id": 13,
        "class_number": {
            "class_num": "10"
        },
        "subject": {
            "id": 1,
            "subjects": "Ingliz Tili",
            "teacher": 26
        },
        "ratings": 5,
        "teacher": 26,
        "pupil": {
            "username": "Begzod",
            "role": "pupil"
        }
    },
    {
        "id": 14,
        "class_number": {
            "class_num": "10"
        },
        "subject": {
            "id": 2,
            "subjects": "Ona Tili",
            "teacher": 26
        },
        "ratings": 4,
        "teacher": 26,
        "pupil": {
            "username": "Begzod",
            "role": "pupil"
        }
    }
]
class App extends Component {
    constructor(props) {
    super(props);
    this.state = { list };
}
    render() {
    return (
    <div>
    {this.state.list.map(item => (
    <div key={item.id}>
    <h1>{item.subject}</h1>
    <p>{item.ratings}</p>
    </div>
    ))}
    </div>
    );
    }
}
export default App;