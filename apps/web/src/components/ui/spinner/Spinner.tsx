import type { HTMLAttributes } from "react";

import { cn } from "@/lib/utils";

type SpinnerProps = HTMLAttributes<HTMLDivElement> & {
  size?: "sm" | "md" | "lg";
};

export default function Spinner({
  size = "md",
  className,
  ...props
}: SpinnerProps) {
  const sizes = {
    sm: "h-4 w-4 border-2",
    md: "h-6 w-6 border-2",
    lg: "h-8 w-8 border-3",
  };

  return (
    <div
      role="status"
      aria-label="Loading"
      className={cn(
        "animate-spin rounded-full border-border border-t-primary",
        sizes[size],
        className,
      )}
      {...props}
    />
  );
}