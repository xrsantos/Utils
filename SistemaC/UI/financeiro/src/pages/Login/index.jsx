import React, { useState, useContext } from "react";

import { AuthContext } from "../../contexts/auth"



const Login = () => {
    const {auth, login} = useContext(AuthContext);

    const [email, setEmail] = useState("");
    const [pass, setPass] = useState("");
    
    const SendLogin = (e) => {
        e.preventDefault();
        console.log("SendLogin");
        login(email,pass);
    }


    return <div className="container mt-5">
                <div className="row justify-content-center">
                    <div className="col-md-6">
                        <h1 className="text-center mb-4">Faça o login</h1>
                        <form onSubmit={SendLogin}>
                            <div className="form-group">
                                <label>E-mail</label>
                                <input key="email" type="email" className="form-control" id="email" placeholder="Informe o seu e-mail" 
                                value={email} 
                                onChange={(e) => setEmail(e.target.value)}
                                required
                                />
                            </div>
                            <div className="form-group">
                                <label>Senha</label>
                                <input key="password" type="password" className="form-control" id="senha" placeholder="Informe a sua senha" 
                                value={pass} 
                                onChange={(e) => setPass(e.target.value)}
                                />
                            </div>
                            <button key="btnsubmit" type="submit" className="btn btn-primary btn-block">Entrar</button>
                            <p>{String(auth)}</p>
                        </form>
                    </div>
                </div>
            </div>

    
    ;
};

export default Login;
