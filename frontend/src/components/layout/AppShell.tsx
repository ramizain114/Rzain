import { useDirection } from '../../hooks/useDirection'
import Sidebar from './Sidebar'
import Navbar from './Navbar'

interface AppShellProps {
  children: React.ReactNode
}

export default function AppShell({ children }: AppShellProps) {
  useDirection()

  return (
    <div className="flex h-screen overflow-hidden bg-background">
      <Sidebar />
      <div className="flex flex-1 flex-col overflow-hidden">
        <Navbar />
        <main className="flex-1 overflow-y-auto p-6">{children}</main>
      </div>
    </div>
  )
}
