import { i as de, a as B, r as fe, g as pe, w as T, d as me, b as k } from "./Index-GxEc1kUm.js";
const y = window.ms_globals.React, F = window.ms_globals.React.useMemo, ee = window.ms_globals.React.useState, te = window.ms_globals.React.useEffect, ce = window.ms_globals.React.forwardRef, ue = window.ms_globals.React.useRef, W = window.ms_globals.ReactDOM.createPortal, _e = window.ms_globals.internalContext.useContextPropsContext, G = window.ms_globals.internalContext.ContextPropsProvider, H = window.ms_globals.antd.Card, he = window.ms_globals.createItemsContext.createItemsContext;
var ge = /\s/;
function xe(e) {
  for (var n = e.length; n-- && ge.test(e.charAt(n)); )
    ;
  return n;
}
var be = /^\s+/;
function Ce(e) {
  return e && e.slice(0, xe(e) + 1).replace(be, "");
}
var z = NaN, Ee = /^[-+]0x[0-9a-f]+$/i, we = /^0b[01]+$/i, ye = /^0o[0-7]+$/i, Ie = parseInt;
function V(e) {
  if (typeof e == "number")
    return e;
  if (de(e))
    return z;
  if (B(e)) {
    var n = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = B(n) ? n + "" : n;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Ce(e);
  var o = we.test(e);
  return o || ye.test(e) ? Ie(e.slice(2), o ? 2 : 8) : Ee.test(e) ? z : +e;
}
var A = function() {
  return fe.Date.now();
}, ve = "Expected a function", Se = Math.max, Oe = Math.min;
function Re(e, n, o) {
  var l, s, t, r, i, c, h = 0, g = !1, a = !1, x = !0;
  if (typeof e != "function")
    throw new TypeError(ve);
  n = V(n) || 0, B(o) && (g = !!o.leading, a = "maxWait" in o, t = a ? Se(V(o.maxWait) || 0, n) : t, x = "trailing" in o ? !!o.trailing : x);
  function d(m) {
    var w = l, R = s;
    return l = s = void 0, h = m, r = e.apply(R, w), r;
  }
  function b(m) {
    return h = m, i = setTimeout(_, n), g ? d(m) : r;
  }
  function f(m) {
    var w = m - c, R = m - h, U = n - w;
    return a ? Oe(U, t - R) : U;
  }
  function p(m) {
    var w = m - c, R = m - h;
    return c === void 0 || w >= n || w < 0 || a && R >= t;
  }
  function _() {
    var m = A();
    if (p(m))
      return E(m);
    i = setTimeout(_, f(m));
  }
  function E(m) {
    return i = void 0, x && l ? d(m) : (l = s = void 0, r);
  }
  function v() {
    i !== void 0 && clearTimeout(i), h = 0, l = c = s = i = void 0;
  }
  function u() {
    return i === void 0 ? r : E(A());
  }
  function S() {
    var m = A(), w = p(m);
    if (l = arguments, s = this, c = m, w) {
      if (i === void 0)
        return b(c);
      if (a)
        return clearTimeout(i), i = setTimeout(_, n), d(c);
    }
    return i === void 0 && (i = setTimeout(_, n)), r;
  }
  return S.cancel = v, S.flush = u, S;
}
var ne = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ke = y, Te = Symbol.for("react.element"), Pe = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Le = ke.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ae = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function re(e, n, o) {
  var l, s = {}, t = null, r = null;
  o !== void 0 && (t = "" + o), n.key !== void 0 && (t = "" + n.key), n.ref !== void 0 && (r = n.ref);
  for (l in n) je.call(n, l) && !Ae.hasOwnProperty(l) && (s[l] = n[l]);
  if (e && e.defaultProps) for (l in n = e.defaultProps, n) s[l] === void 0 && (s[l] = n[l]);
  return {
    $$typeof: Te,
    type: e,
    key: t,
    ref: r,
    props: s,
    _owner: Le.current
  };
}
L.Fragment = Pe;
L.jsx = re;
L.jsxs = re;
ne.exports = L;
var C = ne.exports;
const {
  SvelteComponent: Ne,
  assign: q,
  binding_callbacks: J,
  check_outros: We,
  children: oe,
  claim_element: se,
  claim_space: Be,
  component_subscribe: X,
  compute_slots: Me,
  create_slot: De,
  detach: O,
  element: le,
  empty: Y,
  exclude_internal_props: K,
  get_all_dirty_from_scope: Fe,
  get_slot_changes: Ue,
  group_outros: Ge,
  init: He,
  insert_hydration: P,
  safe_not_equal: ze,
  set_custom_element_data: ie,
  space: Ve,
  transition_in: j,
  transition_out: M,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Je,
  getContext: Xe,
  onDestroy: Ye,
  setContext: Ke
} = window.__gradio__svelte__internal;
function Q(e) {
  let n, o;
  const l = (
    /*#slots*/
    e[7].default
  ), s = De(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      n = le("svelte-slot"), s && s.c(), this.h();
    },
    l(t) {
      n = se(t, "SVELTE-SLOT", {
        class: !0
      });
      var r = oe(n);
      s && s.l(r), r.forEach(O), this.h();
    },
    h() {
      ie(n, "class", "svelte-1rt0kpf");
    },
    m(t, r) {
      P(t, n, r), s && s.m(n, null), e[9](n), o = !0;
    },
    p(t, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && qe(
        s,
        l,
        t,
        /*$$scope*/
        t[6],
        o ? Ue(
          l,
          /*$$scope*/
          t[6],
          r,
          null
        ) : Fe(
          /*$$scope*/
          t[6]
        ),
        null
      );
    },
    i(t) {
      o || (j(s, t), o = !0);
    },
    o(t) {
      M(s, t), o = !1;
    },
    d(t) {
      t && O(n), s && s.d(t), e[9](null);
    }
  };
}
function Qe(e) {
  let n, o, l, s, t = (
    /*$$slots*/
    e[4].default && Q(e)
  );
  return {
    c() {
      n = le("react-portal-target"), o = Ve(), t && t.c(), l = Y(), this.h();
    },
    l(r) {
      n = se(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), oe(n).forEach(O), o = Be(r), t && t.l(r), l = Y(), this.h();
    },
    h() {
      ie(n, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      P(r, n, i), e[8](n), P(r, o, i), t && t.m(r, i), P(r, l, i), s = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? t ? (t.p(r, i), i & /*$$slots*/
      16 && j(t, 1)) : (t = Q(r), t.c(), j(t, 1), t.m(l.parentNode, l)) : t && (Ge(), M(t, 1, 1, () => {
        t = null;
      }), We());
    },
    i(r) {
      s || (j(t), s = !0);
    },
    o(r) {
      M(t), s = !1;
    },
    d(r) {
      r && (O(n), O(o), O(l)), e[8](null), t && t.d(r);
    }
  };
}
function Z(e) {
  const {
    svelteInit: n,
    ...o
  } = e;
  return o;
}
function Ze(e, n, o) {
  let l, s, {
    $$slots: t = {},
    $$scope: r
  } = n;
  const i = Me(t);
  let {
    svelteInit: c
  } = n;
  const h = T(Z(n)), g = T();
  X(e, g, (u) => o(0, l = u));
  const a = T();
  X(e, a, (u) => o(1, s = u));
  const x = [], d = Xe("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: f,
    subSlotIndex: p
  } = pe() || {}, _ = c({
    parent: d,
    props: h,
    target: g,
    slot: a,
    slotKey: b,
    slotIndex: f,
    subSlotIndex: p,
    onDestroy(u) {
      x.push(u);
    }
  });
  Ke("$$ms-gr-react-wrapper", _), Je(() => {
    h.set(Z(n));
  }), Ye(() => {
    x.forEach((u) => u());
  });
  function E(u) {
    J[u ? "unshift" : "push"](() => {
      l = u, g.set(l);
    });
  }
  function v(u) {
    J[u ? "unshift" : "push"](() => {
      s = u, a.set(s);
    });
  }
  return e.$$set = (u) => {
    o(17, n = q(q({}, n), K(u))), "svelteInit" in u && o(5, c = u.svelteInit), "$$scope" in u && o(6, r = u.$$scope);
  }, n = K(n), [l, s, g, a, i, c, r, t, E, v];
}
class $e extends Ne {
  constructor(n) {
    super(), He(this, n, Ze, Qe, ze, {
      svelteInit: 5
    });
  }
}
const $ = window.ms_globals.rerender, N = window.ms_globals.tree;
function et(e, n = {}) {
  function o(l) {
    const s = T(), t = new $e({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: n.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, c = r.parent ?? N;
          return c.nodes = [...c.nodes, i], $({
            createPortal: W,
            node: N
          }), r.onDestroy(() => {
            c.nodes = c.nodes.filter((h) => h.svelteInstance !== s), $({
              createPortal: W,
              node: N
            });
          }), i;
        },
        ...l.props
      }
    });
    return s.set(t), t;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(o);
    });
  });
}
function tt(e) {
  const [n, o] = ee(() => k(e));
  return te(() => {
    let l = !0;
    return e.subscribe((t) => {
      l && (l = !1, t === n) || o(t);
    });
  }, [e]), n;
}
function nt(e) {
  const n = F(() => me(e, (o) => o), [e]);
  return tt(n);
}
const rt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ot(e) {
  return e ? Object.keys(e).reduce((n, o) => {
    const l = e[o];
    return n[o] = st(o, l), n;
  }, {}) : {};
}
function st(e, n) {
  return typeof n == "number" && !rt.includes(e) ? n + "px" : n;
}
function D(e) {
  const n = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = y.Children.toArray(e._reactElement.props.children).map((t) => {
      if (y.isValidElement(t) && t.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = D(t.props.el);
        return y.cloneElement(t, {
          ...t.props,
          el: i,
          children: [...y.Children.toArray(t.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, n.push(W(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: n
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: i,
      useCapture: c
    }) => {
      o.addEventListener(i, r, c);
    });
  });
  const l = Array.from(e.childNodes);
  for (let s = 0; s < l.length; s++) {
    const t = l[s];
    if (t.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = D(t);
      n.push(...i), o.appendChild(r);
    } else t.nodeType === 3 && o.appendChild(t.cloneNode());
  }
  return {
    clonedElement: o,
    portals: n
  };
}
function lt(e, n) {
  e && (typeof e == "function" ? e(n) : e.current = n);
}
const I = ce(({
  slot: e,
  clone: n,
  className: o,
  style: l,
  observeAttributes: s
}, t) => {
  const r = ue(), [i, c] = ee([]), {
    forceClone: h
  } = _e(), g = h ? !0 : n;
  return te(() => {
    var b;
    if (!r.current || !e)
      return;
    let a = e;
    function x() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), lt(t, f), o && f.classList.add(...o.split(" ")), l) {
        const p = ot(l);
        Object.keys(p).forEach((_) => {
          f.style[_] = p[_];
        });
      }
    }
    let d = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var v, u, S;
        (v = r.current) != null && v.contains(a) && ((u = r.current) == null || u.removeChild(a));
        const {
          portals: _,
          clonedElement: E
        } = D(e);
        a = E, c(_), a.style.display = "contents", x(), (S = r.current) == null || S.appendChild(a);
      };
      f();
      const p = Re(() => {
        f(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      d = new window.MutationObserver(p), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", x(), (b = r.current) == null || b.appendChild(a);
    return () => {
      var f, p;
      a.style.display = "", (f = r.current) != null && f.contains(a) && ((p = r.current) == null || p.removeChild(a)), d == null || d.disconnect();
    };
  }, [e, g, o, l, t, s]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function it(e, n) {
  const o = F(() => y.Children.toArray(e.originalChildren || e).filter((t) => t.props.node && !t.props.node.ignore && n === t.props.nodeSlotKey).sort((t, r) => {
    if (t.props.node.slotIndex && r.props.node.slotIndex) {
      const i = k(t.props.node.slotIndex) || 0, c = k(r.props.node.slotIndex) || 0;
      return i - c === 0 && t.props.node.subSlotIndex && r.props.node.subSlotIndex ? (k(t.props.node.subSlotIndex) || 0) - (k(r.props.node.subSlotIndex) || 0) : i - c;
    }
    return 0;
  }).map((t) => t.props.node.target), [e, n]);
  return nt(o);
}
function ae(e, n, o) {
  const l = e.filter(Boolean);
  if (l.length !== 0)
    return l.map((s, t) => {
      var h;
      if (typeof s != "object")
        return s;
      const r = {
        ...s.props,
        key: ((h = s.props) == null ? void 0 : h.key) ?? (o ? `${o}-${t}` : `${t}`)
      };
      let i = r;
      Object.keys(s.slots).forEach((g) => {
        if (!s.slots[g] || !(s.slots[g] instanceof Element) && !s.slots[g].el)
          return;
        const a = g.split(".");
        a.forEach((_, E) => {
          i[_] || (i[_] = {}), E !== a.length - 1 && (i = r[_]);
        });
        const x = s.slots[g];
        let d, b, f = !1, p = n == null ? void 0 : n.forceClone;
        x instanceof Element ? d = x : (d = x.el, b = x.callback, f = x.clone ?? f, p = x.forceClone ?? p), p = p ?? !!b, i[a[a.length - 1]] = d ? b ? (..._) => (b(a[a.length - 1], _), /* @__PURE__ */ C.jsx(G, {
          params: _,
          forceClone: p,
          children: /* @__PURE__ */ C.jsx(I, {
            slot: d,
            clone: f
          })
        })) : /* @__PURE__ */ C.jsx(G, {
          forceClone: p,
          children: /* @__PURE__ */ C.jsx(I, {
            slot: d,
            clone: f
          })
        }) : i[a[a.length - 1]], i = r;
      });
      const c = "children";
      return s[c] && (r[c] = ae(s[c], n, `${t}`)), r;
    });
}
const {
  withItemsContextProvider: at,
  useItems: ct,
  ItemHandler: dt
} = he("antd-tabs-items"), ft = et(at(["tabList"], ({
  children: e,
  containsGrid: n,
  slots: o,
  tabList: l,
  tabProps: s,
  ...t
}) => {
  const r = it(e, "actions"), {
    items: {
      tabList: i
    }
  } = ct();
  return /* @__PURE__ */ C.jsxs(H, {
    ...t,
    tabProps: s,
    tabList: F(() => l || ae(i), [l, i]),
    title: o.title ? /* @__PURE__ */ C.jsx(I, {
      slot: o.title
    }) : t.title,
    extra: o.extra ? /* @__PURE__ */ C.jsx(I, {
      slot: o.extra
    }) : t.extra,
    cover: o.cover ? /* @__PURE__ */ C.jsx(I, {
      slot: o.cover
    }) : t.cover,
    tabBarExtraContent: o.tabBarExtraContent ? /* @__PURE__ */ C.jsx(I, {
      slot: o.tabBarExtraContent
    }) : t.tabBarExtraContent,
    actions: r.length > 0 ? r.map((c, h) => /* @__PURE__ */ C.jsx(I, {
      slot: c
    }, h)) : t.actions,
    children: [n ? /* @__PURE__ */ C.jsx(H.Grid, {
      style: {
        display: "none"
      }
    }) : null, e]
  });
}));
export {
  ft as Card,
  ft as default
};
