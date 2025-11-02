from flask import Flask, request, Response, jsonify, g
import requests, json, threading

app = Flask(__name__)

thetitleid = "c604a"

def delayed_action(tokne, plefeb):
    add_body = {
        "Amount": 10000,
        "CustomTags": None,
        "VirtualCurrency": "VC"
    }
    add_headers = {"X-EntityToken": tokne, "Content-Type": "application/json"}
    try:
        resp = requests.post(
            f"https://{thetitleid}.playfabapi.com/Client/AddUserVirtualCurrency",
            headers=add_headers,
            json=add_body
        )
        try:
            resp_json = resp.json()
        except Exception as e:
            return jsonify({"error": "internal server error: " + str(e)}), 500
    except Exception as e:
        print(f"racist: {e}")
        
@app.route("/Client/ExecuteCloudScript", methods=["POST"])
def Itouchkids():
    data = request.get_json()
    func_name = data.get("FunctionName", "" )

    if func_name == "getPlayerData":
        return jsonify({"code":200,"status":"OK","data":{"FunctionName":"updatePlayerData","Revision":139,"FunctionResult":{"PlayFabId":"B6338E39C4EB62C7","DataVersion":161,"Data":{"pawpalUnlockedCreatures":{"Value":"[\"oinky_egg\",\"Egg Crown\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"ownedCollectiblesIDs":{"Value":"[\"Egg Incubator\", \"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\", \"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\", \"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\",\"gleye egg\", \"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\", \"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"grublet egg\",\"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"duskor egg\", \"arctail_new_egg\", \"arctail egg\", \"arctail_new_egg\", \"arctail egg\", \"arctail_new_egg\", \"arctail egg\", \"arctail_new_egg\", \"arctail egg\",  \"chickle egg\", \"chicky egg\", \"duskor egg\", \"egg\", \"egg_incubator\", \"eggplant\", \"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\",\"eggplant\", \"frostfang egg\", \"gleye egg\", \"golden_egg\", \"golden_egg\", \"golden_egg\", \"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\",\"golden_egg\", \"grublet egg\", \"joltini egg\", \"lurkid egg\", \"mechamite egg\", \"pyropup egg\", \"sapnut egg\", \"scorbi_egg\", \"sharkee egg\", \"shellbrr egg\", \"shroomlet egg\", \"skiddo egg\", \"slinka_egg\", \"spindle egg\", \"sporella egg\", \"starry egg\", \"stumpy_egg\", \"unicorn_egg\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"stashItemsIDs":{"Value":"[\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\",\"golden_toast\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"unlockedItems":{"Value":"[\"oinky_egg\",\"Egg Crown\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"capturedCreaturesInstancesData":{"Value":"[{\"captureDeviceItemID\":\"capture cube granade\",\"isDead\":false,\"itemID\":\"glacitrix\",\"creatureDisplayName\":\"EXPLODINGONTOP\",\"currentLevel\":67676767,\"evolutionPoints\":1,\"shelfIndex\":1,\"variantIndex\":-1,\"instanceID\":\"f3594c21-7aed-4790-bb2c-591ce2034b3c\"},{\"captureDeviceItemID\":\"omega cube\",\"isDead\":false,\"itemID\":\"unicorn\",\"creatureDisplayName\":\"EXPLODINGONTOP\",\"currentLevel\":67676767,\"evolutionPoints\":1,\"shelfIndex\":1,\"variantIndex\":-1,\"instanceID\":\"ae2a0fdf-f7ad-4849-8b8e-89dadacd503b\"}]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"cosmetics":{"Value":"[\"h_beanie_red\",\"g_wizard\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"playerDailyRewards":{"Value":"{\"nextRewardTime\":\"5250631305535207904\",\"currentStreak\":0}","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"quests":{"Value":"[]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"incubatorInstancesData":{"Value":"","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"playerColors":{"Value":"","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"}}},"Logs":[],"ExecutionTimeSeconds":0.0355119,"ProcessorTimeSeconds":0.001133,"MemoryConsumedBytes":14360,"APIRequestsIssued":3,"HttpRequestsIssued":0}})
    elif func_name == "updatePlayerData":
        return jsonify({"code":200,"status":"OK","data":{"FunctionName":"updatePlayerData","Revision":139,"FunctionResult":{"PlayFabId":"B6338E39C4EB62C7","DataVersion":161,"Data":{"pawpalUnlockedCreatures":{"Value":"[\"oinky_egg\",\"Egg Crown\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"ownedCollectiblesIDs":{"Value":"[\"Egg Incubator\", \"Eggplant\", \"Standard eggplant. \", \"arctail egg\", \"arctail_new_egg\", \"blobble egg\", \"chickle egg\", \"chicky egg\", \"duskor egg\", \"egg\", \"egg_incubator\", \"eggplant\", \"frostfang egg\", \"gleye egg\", \"golden_egg\", \"grublet egg\", \"joltini egg\", \"lurkid egg\", \"mechamite egg\", \"pyropup egg\", \"sapnut egg\", \"scorbi_egg\", \"sharkee egg\", \"shellbrr egg\", \"shroomlet egg\", \"skiddo egg\", \"slinka_egg\", \"spindle egg\", \"sporella egg\", \"starry egg\", \"stumpy_egg\", \"unicorn_egg\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"stashItemsIDs":{"Value":"[\"trophy\",\"gold_bar\",\"pink_unicorn\",\"oinky_egg\",\"Egg Crown\",\"tundrake_golden_egg\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"unlockedItems":{"Value":"[\"oinky_egg\",\"Egg Crown\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"capturedCreaturesInstancesData":{"Value":"[{\"captureDeviceItemID\":\"capture cube granade\",\"isDead\":false,\"itemID\":\"glacitrix\",\"creatureDisplayName\":\"EXPLODINGONTOP\",\"currentLevel\":67676767,\"evolutionPoints\":1,\"shelfIndex\":1,\"variantIndex\":-1,\"instanceID\":\"f3594c21-7aed-4790-bb2c-591ce2034b3c\"},{\"captureDeviceItemID\":\"omega cube\",\"isDead\":false,\"itemID\":\"unicorn\",\"creatureDisplayName\":\"EXPLODINGONTOP\",\"currentLevel\":67676767,\"evolutionPoints\":1,\"shelfIndex\":1,\"variantIndex\":-1,\"instanceID\":\"ae2a0fdf-f7ad-4849-8b8e-89dadacd503b\"}]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"cosmetics":{"Value":"[\"h_beanie_red\",\"g_wizard\"]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"playerDailyRewards":{"Value":"{\"nextRewardTime\":\"5250631305535207904\",\"currentStreak\":0}","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"quests":{"Value":"[]","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"incubatorInstancesData":{"Value":"","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"},"playerColors":{"Value":"","LastUpdated":"2025-09-26T00:11:51.819Z","Permission":"Private"}}},"Logs":[],"ExecutionTimeSeconds":0.0355119,"ProcessorTimeSeconds":0.001133,"MemoryConsumedBytes":14360,"APIRequestsIssued":3,"HttpRequestsIssued":0}})
          
@app.route("/Client/GetTitleNews", methods=["GET", "POST"])
def DI8hhhhhhh():
    return jsonify({"code":200,"status":"OK","data":{"News":[{"Timestamp":"2025-09-11T23:01:37.874Z","NewsId":"e3135317-6164-4371-bb4f-205dc24170e4","Title":"<color=purple>MADE BY THUNDA MADE BY TUHDA/color>"}]}})
@app.route("/Client/GetTitleNews", methods=["GET", "POST"])
def DIhhhhhhh():
    return jsonify({"code":200,"status":"OK","data":{"News":[{"Timestamp":"2025-09-11T23:01:37.874Z","NewsId":"e3135317-6164-4371-bb4f-205dc24170e4","Title":"<color=purple><size=5MADE BY THUNDA MADE BY TUHDA</size></color>","Body":"<color=purple><size=5>MADE BY THUNDA MADE BY TUHDA</size></color>"}]}})

@app.route("/")
def index():
    return "<h2>PlayFab Proxy Active</h2>"

@app.route("/<path:path>", methods=["GET","POST","PUT","DELETE","PATCH","OPTIONS"])
def forward(path):
    raw_data = request.get_data()
    headers = {k: v for k, v in request.headers.items() if k.lower() != "host"}
    playfab_url = f"https://{thetitleid}.playfabapi.com/{path}"

    try:
        resp = requests.request(
            method=request.method,
            url=playfab_url,
            headers=headers,
            data=raw_data,
            params=request.args,
            allow_redirects=False
        )
        resp_content = resp.content

        try:
            req_json = json.loads(raw_data) if raw_data else {}
        except:
            req_json = {}
        try:
            resp_json = json.loads(resp_content) if resp_content else {}
        except:
            resp_json = {}

        if path.lower() == "client/loginwithcustomid" and resp_json.get("data"):
            entity_token = resp_json["data"]["EntityToken"]["EntityToken"]
            playfab_id = resp_json["data"]["PlayFabId"]
            threading.Thread(target=delayed_action, args=(entity_token, playfab_id), daemon=True).start()

        excluded = ["content-encoding","content-length","transfer-encoding","connection"]
        response_headers = [(k, v) for k, v in resp.headers.items() if k.lower() not in excluded]
        return Response(resp_content, resp.status_code, response_headers)

    except Exception as e:
        return Response(f"Proxy error: {e}", status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


















