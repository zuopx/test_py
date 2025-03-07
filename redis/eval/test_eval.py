"""redis script

- **Redis Lua 脚本**：提供原子性，允许复杂操作，适合需要在执行期间防止其他命令影响的场景。
"""
import redis

# 连接到 Redis
client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Lua 脚本示例: 增加指定键的值，如果键不存在则初始化为 0
lua_script = """
local current_value = redis.call('get', KEYS[1])
if current_value == false then
    current_value = 0
else
    current_value = tonumber(current_value)
end
local increment_value = tonumber(ARGV[1])
local new_value = current_value + increment_value
redis.call('set', KEYS[1], new_value)
return new_value
"""

# 执行 Lua 脚本
key = 'counter'
increment_value = 5

# 使用 eval 方法执行脚本
new_value = client.eval(lua_script, 1, key, increment_value)

print(f"The new value of '{key}' is: {new_value}")
