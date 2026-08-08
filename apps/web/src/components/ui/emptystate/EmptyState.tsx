import type { HTMLAttributes, ReactNode } from "react";

import { cn } from "@/lib/utils";

type EmptyStateProps = HTMLAttributes<HTMLDivElement> & {
  title: ReactNode;
  description?: ReactNode;
  action?: ReactNode;
};

export default function EmptyState({
  title,
  description,
  action,
  className,
  ...props
}: EmptyStateProps) {
  return (
    <div
      className={cn(
        "flex flex-col items-center justify-center rounded-lg border border-dashed border-border bg-surface px-6 py-12 text-center",
        className,
      )}
      {...props}
    >
      <h2 className="text-lg font-semibold text-text">
        {title}
      </h2>

      {description ? (
        <p className="mt-2 max-w-md text-sm leading-6 text-text-secondary">
          {description}
        </p>
      ) : null}

      {action ? (
        <div className="mt-6">
          {action}
        </div>
      ) : null}
    </div>
  );
}