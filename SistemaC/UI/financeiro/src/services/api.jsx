import axios from "axios";

export const api = axios.create({baseURL: 'http://localhost:8080'})

export const createSession = async(user, password) => {
    return api.post('/api/session',{user: user, password: password})
}