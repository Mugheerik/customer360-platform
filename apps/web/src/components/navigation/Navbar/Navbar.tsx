import { Link, useNavigate } from "react-router-dom";

import Button from "@/components/ui/button";
import { useAuthStore } from "@/store/auth.store";

import { navigation } from "./navigation";

export default function Navbar() {
  const navigate = useNavigate();

  const isAuthenticated = useAuthStore(
    (state) => state.isAuthenticated,
  );

  const clearSession = useAuthStore(
    (state) => state.clearSession,
  );

  function handleLogout() {
    clearSession();
    navigate("/login");
  }

  return (
    <header className="border-b border-border bg-white">
      <div className="mx-auto flex h-16 w-full max-w-[1280px] items-center justify-between px-6">
        <Link
          to={isAuthenticated ? "/dashboard" : "/"}
          className="text-lg font-semibold text-text"
        >
          Customer360
        </Link>

        <nav className="flex items-center gap-6">
          {navigation.map((item) => (
            <Link
              key={item.href}
              to={item.href}
              className="text-sm font-medium text-text-secondary transition-colors hover:text-text"
            >
              {item.label}
            </Link>
          ))}

          {isAuthenticated ? (
            <Button
              variant="secondary"
              type="button"
              onClick={handleLogout}
            >
              Logout
            </Button>
          ) : (
            <>
              <Button
                variant="secondary"
                type="button"
                onClick={() => navigate("/register")}
              >
                Register
              </Button>

              <Button
                type="button"
                onClick={() => navigate("/login")}
              >
                Sign In
              </Button>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}