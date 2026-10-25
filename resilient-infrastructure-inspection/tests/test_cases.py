"""Run from project root: python -m unittest discover -s tests -v"""
import json
import unittest
from pathlib import Path
from ai_modules.bfs import bfs
from ai_modules.astar import astar
from ai_modules.csp import solve_csp
from ai_modules.knowledge_base import infer

BASE = Path(__file__).resolve().parents[1]

def load(name):
    with open(BASE / "data" / name, encoding="utf-8") as f:
        return json.load(f)

def graph_from(roads, blocked=None):
    graph, blocked = {}, blocked or set()
    for r in roads:
        a, b, cost = r["from"], r["to"], r["cost"]
        if frozenset((a,b)) in blocked:
            continue
        graph.setdefault(a, []).append((b,cost))
        graph.setdefault(b, []).append((a,cost))
    return graph

class ProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sites, cls.roads, cls.crews = load("sites.json"), load("roads.json"), load("crews.json")

    def test_astar_cost_not_more_than_bfs_path(self):
        g = graph_from(self.roads)
        self.assertEqual(astar(g, "A", "E")["cost"], 5)
        self.assertGreaterEqual(bfs(g, "A", "E")["cost"], astar(g, "A", "E")["cost"])

    def test_blocked_road_still_route_if_connected(self):
        g = graph_from(self.roads, {frozenset(("B","C"))})
        self.assertTrue(astar(g, "A", "E")["path"])

    def test_csp_assigns_every_task_when_crews_available(self):
        result = solve_csp(self.sites, self.crews)
        self.assertTrue(result["success"])
        self.assertEqual(len(result["assignment"]), len(self.sites))

    def test_knowledge_base_flags_high_risk_sites(self):
        result = infer(self.sites, self.crews)
        self.assertIn("S1", result["high_priority_sites"])
        self.assertIn("S4", result["urgent_structural_sites"])

if __name__ == "__main__":
    unittest.main()
