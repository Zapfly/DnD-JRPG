// import { useState, useEffect } from "react";

export const fetchFunc = async (url = '', urlMethod = 'GET', data = {}) => {
    const response = await fetch(url, {
        method: urlMethod,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

export const fetchFuncAuth = async (url = '', urlMethod = 'GET', token, data = {}) => {
    const response = await fetch(url, {
        method: urlMethod,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

export const fetchPostWithAuth = async (url = '', urlMethod = 'POST', token, data = {}) => {
    const response = await fetch(url, {
        method: urlMethod,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

// export const useFetchWithAuth = (url = '', urlMethod = 'GET', token = '', inputData = {}) => {
//     const [data, setData] = useState(null);
//     const [loading, setLoading] = useState(true);

//     useEffect(() => {
//         const fetchData = async () => {
//             const response = await fetch(url, {
//                 method: `${urlMethod}`,
//                 headers: {
//                     'Authorization': `Bearer ${token}`
//                 },
//                 body: JSON.stringify(inputData)
//             });
//             const data = await response.json();
//             const [item] = data.results;
//             setData(item);
//             setLoading(false);
//         }
//         fetchData();
//     }, []);

//     return { data, loading };
// };