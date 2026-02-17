#!/bin/bash
# Amana-GRC Testing Startup Script

echo "🚀 Starting Amana-GRC Platform..."
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Error: Docker is not running. Please start Docker first."
    exit 1
fi

echo "✅ Docker is running"
echo ""

# Start services
echo "📦 Starting services (MongoDB, Redis, Backend, Frontend)..."
docker-compose up -d

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

# Create admin user
echo ""
echo "👤 Creating admin user..."
docker-compose exec -T backend python -m app.seeders.create_admin

# Seed standards
echo ""
echo "📚 Loading Saudi regulatory standards..."
docker-compose exec -T backend python -m app.seeders.run_seeders --all

echo ""
echo "✅ Setup complete!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 ACCESS THE APPLICATION:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🌐 Frontend:  http://localhost:3000"
echo "📡 Backend:   http://localhost:8000"
echo "📖 API Docs:  http://localhost:8000/docs"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔐 LOGIN CREDENTIALS:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Username: admin"
echo "Password: Admin@123456"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 LOADED DATA:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ NCA-ECC:  114 Cybersecurity Controls"
echo "✅ NCA-CSCC: 73 Cloud Security Controls"
echo "✅ NDMO:     50 Data Management Controls"
echo "✅ SDAIA:    30 AI Ethics Controls"
echo "✅ Total:    267 Controls"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🧪 TESTING TIPS:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Test language switching (English ↔ Arabic)"
echo "2. View Dashboard metrics"
echo "3. Browse Compliance controls"
echo "4. Create a test risk in Risk Register"
echo "5. Try different view modes (Table/Matrix/Heatmap)"
echo "6. Explore API docs at /docs endpoint"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 See TESTING_GUIDE.md for detailed testing instructions"
echo ""
echo "To view logs: docker-compose logs -f"
echo "To stop: docker-compose down"
echo ""
