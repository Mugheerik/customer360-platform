import type { HTMLAttributes, ReactNode } from "react";

import { cn } from "@/lib/utils";

type PageHeaderProps = HTMLAttributes<HTMLDivElement> & {
  title: ReactNode;
  description?: ReactNode;
  actions?: ReactNode;
};

export default function PageHeader({
  title,
  description,
  actions,
  className,
  ...props
}: PageHeaderProps) {
  return (
    <div
      className={cn(
        "flex flex-col gap-6 border-b border-border pb-6 sm:flex-row sm:items-end sm:justify-between",
        className,
      )}
      {...props}
    >
      <div className="space-y-2">
        <h1 className="text-3xl font-bold tracking-tight text-text">
          {title}
        </h1>

        {description ? (
          <p className="max-w-2xl text-sm leading-6 text-text-secondary">
            {description}
          </p>
        ) : null}
      </div>

      {actions ? (
        <div className="flex shrink-0 items-center gap-3">
          {actions}
        </div>
      ) : null}
    </div>
  );
}