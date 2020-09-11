import React, { useState, useEffect } from "react";

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

export const useFetchWithAuth = (url = '', urlMethod = 'GET', token = '') => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(async () => {
        const response = await fetch(url, {
            method: `${urlMethod}`,
            headers: {
                Authorization: `JWT ${token}`
            }
        });
        const data = await response.json();
        const [item] = data.results;
        setData(item);
        setLoading(false);
    }, []);

    return { data, loading };
};