import os
import requests

def renew_server_time():
    """
    使用 API Key 调用 /api/client/notfreeservers/<id>/renew 接口
    来自动续期 WeirdHost 服务器时间。
    """
    api_key = os.environ.get("WEIRDHOST_API_KEY")
    if not api_key:
        print("❌ 错误: 未设置环境变量 WEIRDHOST_API_KEY。")
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
        return False

    if response.status_code in (200, 204):
        print("✅ 服务器续期成功！")
        return True
    else:
        print(f"❌ 续期失败 ({response.status_code})")
        print("响应内容:", response.text)
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
