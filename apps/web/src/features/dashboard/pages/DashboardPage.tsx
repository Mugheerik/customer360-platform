import {
  Activity,
  ArrowRight,
  Building2,
  Users,
  UserPlus,
} from "lucide-react";
import { useNavigate } from "react-router-dom";

import Button from "@/components/ui/button";
import Card from "@/components/ui/card";
import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { Body, H1, Lead } from "@/components/ui/typography";

type StatCardProps = {
  title: string;
  value: string;
  description: string;
  icon: typeof Users;
};

function StatCard({
  title,
  value,
  description,
  icon: Icon,
}: StatCardProps) {
  return (
    <Card className="p-6">
      <div className="flex items-start justify-between">
        <div>
          <p className="text-sm font-medium text-text-secondary">
            {title}
          </p>

          <p className="mt-2 text-3xl font-semibold tracking-tight text-text">
            {value}
          </p>

          <p className="mt-2 text-sm text-text-secondary">
            {description}
          </p>
        </div>

        <div className="rounded-lg bg-blue-50 p-3">
          <Icon className="h-5 w-5 text-primary" />
        </div>
      </div>
    </Card>
  );
}

export default function DashboardPage() {
  const navigate = useNavigate();

  return (
    <Section>
      <Container>
        <div>
          <H1>Dashboard</H1>

          <Lead className="mt-3">
            Welcome back to Customer360.
          </Lead>

          <Body className="mt-2 max-w-2xl text-text-secondary">
            Monitor your customer platform, review activity, and
            access the tools you need to manage customer relationships.
          </Body>
        </div>

        <div className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <StatCard
            title="Total Customers"
            value="0"
            description="Customers in the platform"
            icon={Users}
          />

          <StatCard
            title="Active Customers"
            value="0"
            description="Currently active customers"
            icon={Activity}
          />

          <StatCard
            title="New Customers"
            value="0"
            description="Added this month"
            icon={UserPlus}
          />

          <StatCard
            title="Organizations"
            value="0"
            description="Customer organizations"
            icon={Building2}
          />
        </div>

        <div className="mt-10 grid gap-6 lg:grid-cols-2">
          <Card className="p-8">
            <div>
              <h2 className="text-lg font-semibold text-text">
                Quick Actions
              </h2>

              <p className="mt-2 text-sm text-text-secondary">
                Common actions for managing your customer platform.
              </p>
            </div>

            <div className="mt-6 flex flex-wrap gap-3">
              <Button
                type="button"
                onClick={() => navigate("/customers")}
              >
                Add Customer
              </Button>

              <Button
                type="button"
                variant="secondary"
                onClick={() => navigate("/customers")}
              >
                View Customers
              </Button>
            </div>
          </Card>

          <Card className="p-8">
            <div>
              <h2 className="text-lg font-semibold text-text">
                Recent Activity
              </h2>

              <p className="mt-2 text-sm text-text-secondary">
                Activity from your customer platform will appear here.
              </p>
            </div>

            <div className="mt-6 rounded-lg border border-border bg-surface p-6">
              <p className="text-sm font-medium text-text">
                No recent activity
              </p>

              <p className="mt-1 text-sm text-text-secondary">
                Customer activity will appear here as the platform is
                used.
              </p>
            </div>
          </Card>
        </div>

        <Card className="mt-10 p-8">
          <div className="flex flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <h2 className="text-lg font-semibold text-text">
                Customer Management
              </h2>

              <p className="mt-2 max-w-xl text-sm text-text-secondary">
                Manage customer records, review customer information,
                and track relationships across the platform.
              </p>
            </div>

            <Button
              type="button"
              variant="secondary"
              onClick={() => navigate("/customers")}
            >
              View Customers
              <ArrowRight className="ml-2 h-4 w-4" />
            </Button>
          </div>
        </Card>
      </Container>
    </Section>
  );
}