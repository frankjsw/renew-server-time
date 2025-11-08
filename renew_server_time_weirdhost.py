import os
import requests

def send_telegram_message(message):
    """
    通过 Telegram Bot 发送消息。
    """
    server_name = "weirdhost"  # 服务器名称
    
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not bot_token or not chat_id:
        print("❌ {server_name} 错误: 未设置 Telegram Bot Token 或 Chat ID。")
        return

    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(telegram_url, params=params)
        if response.status_code == 200:
            print("✅ {server_name}服务器消息发送成功！")
            print("响应内容:", response.text)
        else:
            print(f"❌ {server_name} 服务器消息发送失败: {response.status_code}")
            print("响应内容:", response.text)
    except Exception as e:
        print(f"❌ {server_name}服务器请求失败: {e}")

def renew_server_time():
    """
    使用 API Key 调用 /api/client/notfreeservers/<id>/renew 接口
    来自动续期 WeirdHost 服务器时间。
    """
    api_key = os.environ.get("WEIRDHOST_API_KEY")
    if not api_key:
        print("❌ 错误: 未设置环境变量 WEIRDHOST_API_KEY。")
        send_telegram_message("❌ 服务器续期任务失败：未设置 WEIRDHOST_API_KEY。")
        return False

    server_id = "0f4424f2-3633-4861-b4bf-e2a31ff2067c"
    base_url = "https://hub.weirdhost.xyz"
    renew_url = f"{base_url}/api/client/notfreeservers/{server_id}/renew"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    print(f"🔄 正在向 {renew_url} 发送续期请求...")
    try:
        response = requests.post(renew_url, headers=headers, timeout=15)
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        send_telegram_message(f"❌ {server_name}服务器续期请求失败: {e}")
        return False

    if response.status_code in (200, 204):
        print("✅ {server_name}服务器续期成功！")
        send_telegram_message("✅ {server_name}服务器续期成功！")
        return True
    else:
        print(f"❌ {server_name}续期失败 ({response.status_code})")
        print("响应内容:", response.text)
        send_telegram_message(f"❌ {server_name}服务器续期失败: 状态码 {response.status_code}\n响应内容: {response.text}")
        return False


if __name__ == "__main__":
    print("开始执行服务器续期任务...")
    success = renew_server_time()
    if success:
        print("任务执行成功 ✅")
        exit(0)
    else:
        print("任务执行失败 ❌")
        exit(1)
