import axios from 'axios';

// Use environment variable for the backend URL
// You should change this line:
const API_BASE_URL = 'https://smart-spend-analyzer.onrender.com'; // <--- CHANGE THIS LINE

const api = axios.create({
    baseURL: API_BASE_URL,
});

export const uploadReceipt = async (imageFile, userId) => {
    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('user_id', userId);

    try {
        const response = await api.post('/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error uploading receipt:', error);
        throw error;
    }
};

export const getUserData = async (userId) => {
    try {
        const response = await api.get(`/user/${userId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching user data:', error);
        throw error;
    }
};
