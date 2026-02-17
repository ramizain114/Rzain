import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from './stores/auth-store'
import LoginPage from './pages/LoginPage'
import DashboardPage from './pages/DashboardPage'
import CompliancePage from './pages/CompliancePage'
import RiskRegisterPage from './pages/RiskRegisterPage'
import AppShell from './components/layout/AppShell'

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuthStore()
  
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />
  }
  
  return <>{children}</>
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route
          path="/*"
          element={
            <ProtectedRoute>
              <AppShell>
                <Routes>
                  <Route path="/" element={<Navigate to="/dashboard" replace />} />
                  <Route path="/dashboard" element={<DashboardPage />} />
                  <Route path="/compliance" element={<CompliancePage />} />
                  <Route path="/risks" element={<RiskRegisterPage />} />
                </Routes>
              </AppShell>
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  )
}

export default App
