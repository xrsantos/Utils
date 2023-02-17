import React, { useContext } from "react";
import { useEffect } from "react";
import { AuthContext } from "../../contexts/auth";




const Home = () => {

    useEffect(() =>{
        
    });

    const logout = useContext(AuthContext);
    const handlelogout = () => { 
        logout.logout();
    };
    return <>
        <h1>Home Page</h1>
        <button onClick={handlelogout} className="btn btn-primary">Logout</button>
    </>
};

export default Home;
