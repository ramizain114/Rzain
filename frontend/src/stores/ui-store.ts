import { create } from 'zustand'
import { persist } from 'zustand/middleware'

interface UIState {
  language: 'en' | 'ar'
  sidebarOpen: boolean
  setLanguage: (lang: 'en' | 'ar') => void
  toggleSidebar: () => void
}

export const useUIStore = create<UIState>()(
  persist(
    (set) => ({
      language: 'en',
      sidebarOpen: true,
      setLanguage: (language) => set({ language }),
      toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
    }),
    {
      name: 'ui-storage',
    }
  )
)
