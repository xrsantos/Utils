using Microsoft.AspNetCore.Mvc;

namespace SistemaB.Controllers;

[ApiController]
[Route("[controller]")]
public class AccessController : ControllerBase
{
    [HttpGet(Name = "Login")]
    public bool Login(string username, string password)
    {
        if (string.IsNullOrEmpty(username))
        {
            return false;
        }
        if (username.ToLower() == "ricardo")
        {
            return true;    
        }
        return false;
    }
}
