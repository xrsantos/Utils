//https://www.youtube.com/watch?v=5KqP3Vx8Y4s
import React,{ createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export const AuthContext = createContext();
export const AuthProvider = ({children}) => {
    const navigate = useNavigate();

    const [user , setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(
        () =>{
            const user = localStorage.getItem('userlogger');
            if (user) {
                setUser(JSON.parse(user));
            }
            setLoading(false);
        }
    , []);

    const login = (login, pass) => {
        console.log("login",{login: login, pass: pass});

        if (pass === "123") {
            const result = {Id:"123", email: login};
            setUser(result);
            localStorage.setItem("userlogger", JSON.stringify(result));
            navigate("/");

        }
    }
    const logout = () => {
        console.log("logout");
        localStorage.removeItem("userlogger");

        setUser(null);
        navigate("/login");
    }

    return (    
        <AuthContext.Provider 
            value={{auth: !!user, user, loading, login, logout}} >
                {children}
        </AuthContext.Provider>
    );
}

