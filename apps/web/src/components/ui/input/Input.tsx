import type { InputHTMLAttributes } from "react";

import { cn } from "@/lib/utils";

type InputProps = InputHTMLAttributes<HTMLInputElement>;

export default function Input({
  className,
  ...props
}: InputProps) {
  return (
    <input
      className={cn(
        "w-full rounded-md border border-border bg-background px-3 py-2.5",
        "text-sm text-text placeholder:text-text-secondary",
        "transition-colors duration-200",
        "focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20",
        "disabled:cursor-not-allowed disabled:opacity-50 disabled:bg-surface",
        className,
      )}
      {...props}
    />
  );
}