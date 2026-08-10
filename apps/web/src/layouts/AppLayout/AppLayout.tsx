import { Outlet } from "react-router-dom";

import Navbar from "@/components/navigation/Navbar";

export default function AppLayout() {
  return (
    <div className="min-h-screen bg-background text-text">
      <Navbar />

      <main className="mx-auto w-full max-w-[1280px] px-6 py-8">
        <Outlet />
      </main>
    </div>
  );
}