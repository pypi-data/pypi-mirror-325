import os


def create_app_urls(app_name, project_type):
    if project_type == "Django + RestFramework":
        content = """
from django.urls import path
from .views import HelloWorldAPIView

urlpatterns = [
    path('', HelloWorldAPIView.as_view(), name='hello_world'),
]
"""
    else:
        content = """from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
"""

    with open(os.path.join(app_name, "urls.py"), "w") as f:
        f.write(content)


def create_home_view(app_name, project_type):
    if project_type == "Django + RestFramework":
        content = """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class HelloWorldAPIView(APIView):
    permission_classes = [AllowAny] 
    def get(self, request):
        return Response({"message": "Hello, world!"})
        """
    else:
        content = """from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
"""

    with open(os.path.join(app_name, "views.py"), "w") as f:
        f.write(content)


def update_project_urls(project_name, app_name, project_type):
    project_url_path = os.path.join(project_name, "urls.py")
    with open(project_url_path, "a") as urls_file:
        urls_file.write(f"\nfrom django.urls import include\n")
        urls_file.write(
            f"\nfrom django.conf import settings\nfrom django.conf.urls.static import static\n"
        )

        urls_file.write(f"urlpatterns += [path('', include('{app_name}.urls'))]\n")

        urls_file.write(f"\n# Serve media and static files in development\n")
        urls_file.write(f"if settings.DEBUG:\n")
        urls_file.write(
            f"    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n"
        )
        urls_file.write(
            f"    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\n"
        )
        if project_type == "Django + Channels":
            urls_file.write("\nfrom django.urls import re_path\n")
            urls_file.write(f"from {app_name}.routing import websocket_urlpatterns\n\n")
            urls_file.write(
                "urlpatterns += [re_path(r'^ws/', include(websocket_urlpatterns))]\n"
            )


def create_templates_v2(app_name, project_name, project_type):
    if project_type == "Django + RestFramework":
        return
    templates_dir = os.path.join(os.getcwd(), "templates")
    os.makedirs(templates_dir, exist_ok=True)
    print(f"Templates directory: {templates_dir}")

    # Base HTML template with improved Tailwind styling
    base_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name} | Django-Kickstart</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 text-gray-900 min-h-screen">
    <nav class="bg-blue-600 text-white shadow-lg">
        <div class="container mx-auto py-4 px-6">
            <h1 class="text-2xl font-bold text-center">
                {project_name} - Powered by Django-Kickstart
            </h1>
        </div>
    </nav>
    <main class="container mx-auto px-4 py-8">
        {{% block content %}}
        {{% endblock content %}}
    </main>
</body>
</html>"""

    try:
        with open(
            os.path.join(templates_dir, "base.html"), "w", encoding="utf-8"
        ) as base_file:
            base_file.write(base_html_content)
        print("base.html created successfully.")
    except Exception as e:
        print(f"Failed to create base.html: {e}")

    # Regular Django template
    if project_type != "Django + Channels":
        home_html_content = f"""{{% extends 'base.html' %}}
{{% block content %}}
    <div class="text-center py-10">
        <h1 class="text-5xl font-bold text-blue-600">Welcome to Django-Kickstart</h1>
        <p class="text-lg text-gray-700 mt-4">Effortless Django setup for fast development.</p>
    </div>
    <div class="max-w-3xl mx-auto bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-2xl font-semibold text-gray-800">Next Steps:</h2>
        <ul class="mt-4 space-y-3">
            <li class="bg-gray-50 p-4 rounded-lg shadow-sm">
                <strong>Explore:</strong> Modify <code>{app_name}/views.py</code> to customize views.
            </li>
            <li class="bg-gray-50 p-4 rounded-lg shadow-sm">
                <strong>Routing:</strong> Add URLs in <code>{app_name}/urls.py</code>.
            </li>
            <li class="bg-gray-50 p-4 rounded-lg shadow-sm">
                <strong>Templates:</strong> Update <code>base.html</code> for layout customization.
            </li>
            <li class="bg-gray-50 p-4 rounded-lg shadow-sm">
                <strong>Admin:</strong> Access the Django Admin at <code>/admin</code>.
            </li>
        </ul>
        <h2 class="text-xl font-semibold text-gray-800 mt-6">Need Help?</h2>
        <p class="text-gray-600">Contact us at <a href="mailto:nair.remith@gmail.com" class="text-blue-600">nair.remith@gmail.com</a></p>
    </div>
{{% endblock content %}}"""
    # Channels template
    elif project_type == "Django + Channels":
        home_html_content = f"""{{% extends 'base.html' %}}
{{% block content %}}
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
    <!-- Calculator Section -->
    <div class="bg-white rounded-xl shadow-lg p-6">
        <h2 class="text-2xl font-bold mb-6 text-gray-800 text-center">Live Calculator</h2>
        
        <textarea 
            id="results" 
            class="w-full h-48 p-4 mb-4 rounded-lg bg-gray-50 text-gray-700 resize-none border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            readonly
            placeholder="Calculation results will appear here..."
        ></textarea>
        
        <div class="flex gap-3">
            <input 
                type="text" 
                id="exp" 
                class="flex-1 px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="Enter mathematical expression"
            >
            <button 
                id="submit" 
                class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors duration-200 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
                Calculate
            </button>
        </div>
    </div>

    <!-- Next Steps Section -->
    <div class="bg-white rounded-xl shadow-lg p-6">
        <h2 class="text-2xl font-bold mb-6 text-gray-800">Next Steps</h2>
        <ul class="space-y-4">
                <li class="bg-gray-50 p-4 rounded-lg border border-gray-100 hover:bg-gray-100 transition-colors duration-200">
                    <strong class="text-blue-600">Views:</strong> 
                    <p class="mt-2">Modify <code class="bg-gray-200 px-2 py-1 rounded text-sm">/{app_name}/views.py</code> to customize your views</p>
                </li>
                <li class="bg-gray-50 p-4 rounded-lg border border-gray-100 hover:bg-gray-100 transition-colors duration-200">
                    <strong class="text-blue-600">URLs:</strong> 
                    <p class="mt-2">Configure routes in <code class="bg-gray-200 px-2 py-1 rounded text-sm">/{app_name}/urls.py</code></p>
                </li>
                <li class="bg-gray-50 p-4 rounded-lg border border-gray-100 hover:bg-gray-100 transition-colors duration-200">
                    <strong class="text-blue-600">Templates:</strong> 
                    <p class="mt-2">Update <code>base.html</code> for layout customization.</p>
            <li class="bg-gray-50 p-4 rounded-lg border border-gray-100 hover:bg-gray-100 transition-colors duration-200">
                <strong class="text-blue-600">Routing:</strong> 
                    <p class="mt-2">Configure websocket routes in <code class="bg-gray-200 px-2 py-1 rounded text-sm">/{app_name}/routing.py</code></p>
            </li>
            <li class="bg-gray-50 p-4 rounded-lg border border-gray-100 hover:bg-gray-100 transition-colors duration-200">
                <strong class="text-blue-600">Consumers:</strong> 
                    <p class="mt-2">Modify <code class="bg-gray-200 px-2 py-1 rounded text-sm">/{app_name}/consumers.py</code> to customize your consumers</p>
            </li>
            </li>
                <li class="bg-gray-50 p-4 rounded-lg border border-gray-100 hover:bg-gray-100 transition-colors duration-200">
                    <strong class="text-blue-600">Admin Interface</strong>
                    <p class="mt-2">Access the admin panel at <code class="bg-gray-200 px-2 py-1 rounded text-sm">/admin</code></p>
                </li>
        </ul>
    </div>
</div>

<script>
    const socket = new WebSocket(`ws://localhost:8000/ws/livec/`);
    const resultsArea = document.getElementById("results");
    const expInput = document.getElementById("exp");
    const submitBtn = document.getElementById("submit");

    socket.onmessage = function(e) {{
        const result = JSON.parse(e.data).result;
        resultsArea.value += "Server: " + result + "\\n";
        resultsArea.scrollTop = resultsArea.scrollHeight;
    }}

    socket.onclose = function() {{
        console.log("Socket closed!");
        resultsArea.value += "Connection lost. Please refresh.\\n";
    }}

    expInput.onkeyup = function(e) {{
        if (e.key === 'Enter') {{
            submitBtn.click();
        }}
    }};

    submitBtn.onclick = function() {{
        const exp = expInput.value;
        if (exp.trim()) {{
            socket.send(JSON.stringify({{ expression: exp }}));
            resultsArea.value += "You: " + exp + "\\n";
            expInput.value = "";
            resultsArea.scrollTop = resultsArea.scrollHeight;
        }}
    }}
</script>
{{% endblock content %}}"""

    try:
        with open(
            os.path.join(templates_dir, "home.html"), "w", encoding="utf-8"
        ) as home_file:
            home_file.write(home_html_content)
        print("home.html created successfully.")
    except Exception as e:
        print(f"Failed to create home.html: {e}")
