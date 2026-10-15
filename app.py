
from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {"name": "Stylish T-Shirt", "price": 499, "emoji": "👕"},
    {"name": "Smartphone", "price": 9999, "emoji": "📱"},
    {"name": "Sports Shoes", "price": 1299, "emoji": "👟"},
    {"name": "Headphones", "price": 799, "emoji": "🎧"},
    {"name": "Wrist Watch", "price": 599, "emoji": "⌚"},
    {"name": "Backpack", "price": 899, "emoji": "🎒"},
    {"name": "Sunglasses", "price": 399, "emoji": "🕶️"},
    {"name": "Beauty Kit", "price": 699, "emoji": "💄"},
]

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>HASIM MART | Online Shopping</title>
<style>
*{box-sizing:border-box}
body{margin:0;font-family:Arial;background:#f3f4f6;color:#222}
header{background:#131921;color:white;padding:18px;text-align:center}
header h1{margin:0;color:#ffcc00;font-size:30px}
header p{margin:8px 0 0}
.search{padding:18px;text-align:center;background:#232f3e}
input{width:90%;max-width:500px;padding:13px;border:0;border-radius:7px;font-size:16px}
.hero{background:linear-gradient(120deg,#172554,#2563eb);color:white;padding:35px 15px;text-align:center}
.hero h2{font-size:28px;margin:0 0 10px}
.products{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;padding:15px;max-width:1000px;margin:auto}
.card{background:white;border-radius:12px;padding:18px 10px;text-align:center;box-shadow:0 2px 8px #ddd}
.emoji{font-size:55px}
.card h3{font-size:16px}
.price{font-weight:bold;color:#087443;font-size:19px}
button{background:#ffcc00;border:0;padding:11px;border-radius:20px;font-weight:bold;cursor:pointer}
#cart{background:white;margin:15px;padding:18px;border-radius:10px}
footer{background:#131921;color:white;text-align:center;padding:25px}
@media(min-width:650px){.products{grid-template-columns:repeat(4,minmax(0,1fr))}}
</style>
</head>
<body>
<header>
<h1>🛍️ HASIM MART</h1>
<p>Har Shopping, Ab Aasaan!</p>
</header>
<div class="search">
<input id="search" placeholder="🔍 Search products..." oninput="filterProducts()">
</div>
<section class="hero">
<h2>Welcome to HASIM MART!</h2>
<p>Discover amazing products at great prices.</p>
<button onclick="document.getElementById('shop').scrollIntoView()">Shop Now ↓</button>
</section>
<h2 style="text-align:center">✨ Our Products</h2>
<div class="products" id="shop">
{% for p in products %}
<div class="card" data-name="{{ p.name }}">
<div class="emoji">{{ p.emoji }}</div>
<h3>{{ p.name }}</h3>
<div class="price">₹{{ p.price }}</div>
<br>
<button onclick="addToCart('{{ p.name }}',{{ p.price }})">Add to Cart 🛒</button>
</div>
{% endfor %}
</div>
<div id="cart">
<h2>🛒 Your Cart (<span id="count">0</span>)</h2>
<div id="items">Your cart is empty.</div>
<h3>Total: ₹<span id="total">0</span></h3>
</div>
<footer>
<h3>HASIM MART</h3>
<p>Your own online shopping store.</p>
<p>© 2026 HASIM MART</p>
</footer>
<script>
let cart=[];
function addToCart(name,price){
cart.push({name,price});
document.getElementById('count').textContent=cart.length;
document.getElementById('total').textContent=cart.reduce((s,p)=>s+p.price,0);
document.getElementById('items').innerHTML=cart.map((p,i)=>
'<p>'+p.name+' — ₹'+p.price+
' <button onclick="removeItem('+i+')">Remove</button></p>').join('');
}
function removeItem(i){
cart.splice(i,1);
document.getElementById('count').textContent=cart.length;
document.getElementById('total').textContent=cart.reduce((s,p)=>s+p.price,0);
document.getElementById('items').innerHTML=cart.length?cart.map((p,i)=>
'<p>'+p.name+' — ₹'+p.price+
' <button onclick="removeItem('+i+')">Remove</button></p>').join(''):'Your cart is empty.';
}
function filterProducts(){
let q=document.getElementById('search').value.toLowerCase();
document.querySelectorAll('.card').forEach(c=>{
c.style.display=c.dataset.name.toLowerCase().includes(q)?'block':'none';
});
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
