import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class OrdersService {

    constructor() { }

    getOrders() {
        const url = `${API_URL}/api/orders/`;
        return axios.get(url).then(response => response.data);
    }
}