<?php

namespace App\Http\Controllers\Auth\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;



class LoginController extends Controller
{
    public function live(Request $request)
    {
        return response()->json(
            [   'data' 
                => [ 'ok']
            ]);
    }

    public function login(Request $request)
    {
        $credentias = $request->only('email','password');

        if (!auth()->attempt($credentias))
            abort(401,"Invalid Credentials");
        
        $token = $request->user()->createToken('AccessID');
        
        return response()->json(
            [   'data' 
                => [ 'token' => $token->plainTextToken ]
            ]);
    }
}
