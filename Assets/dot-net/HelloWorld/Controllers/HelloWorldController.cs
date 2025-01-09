using Microsoft.AspNetCore.Mvc;

namespace HelloWorldApi.Controllers
{
    // 这里api/[contorller] 
    // 如果是Class HelloWorldController，默认路由就是 api/HelloWorld
    [ApiController]
    [Route("api/[controller]")]
    public class HelloWorldController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetHelloWorld()
        {
            return Ok("Hello World");
        }
    }
    
}
