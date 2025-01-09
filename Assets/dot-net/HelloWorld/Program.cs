var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// 添加控制器服务
builder.Services.AddControllers();

var app = builder.Build();

// Enable Swagger UI in development mode
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// 添加中间件
app.UseHttpsRedirection();

app.UseAuthorization();

// 配置控制器路由
app.MapControllers();

app.Run();
