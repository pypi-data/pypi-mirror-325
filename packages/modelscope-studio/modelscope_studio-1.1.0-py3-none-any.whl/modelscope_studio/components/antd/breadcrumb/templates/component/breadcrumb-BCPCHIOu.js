import { i as ue, a as M, r as de, g as fe, w as k } from "./Index-COxxxGc-.js";
const y = window.ms_globals.React, se = window.ms_globals.React.forwardRef, oe = window.ms_globals.React.useRef, ie = window.ms_globals.React.useState, ce = window.ms_globals.React.useEffect, ae = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, me = window.ms_globals.internalContext.useContextPropsContext, P = window.ms_globals.internalContext.ContextPropsProvider, _e = window.ms_globals.antd.Breadcrumb, he = window.ms_globals.createItemsContext.createItemsContext;
var ge = /\s/;
function pe(t) {
  for (var e = t.length; e-- && ge.test(t.charAt(e)); )
    ;
  return e;
}
var be = /^\s+/;
function xe(t) {
  return t && t.slice(0, pe(t) + 1).replace(be, "");
}
var U = NaN, we = /^[-+]0x[0-9a-f]+$/i, Ce = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, ye = parseInt;
function H(t) {
  if (typeof t == "number")
    return t;
  if (ue(t))
    return U;
  if (M(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = M(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = xe(t);
  var o = Ce.test(t);
  return o || Ee.test(t) ? ye(t.slice(2), o ? 2 : 8) : we.test(t) ? U : +t;
}
var N = function() {
  return de.Date.now();
}, ve = "Expected a function", Ie = Math.max, Re = Math.min;
function Se(t, e, o) {
  var s, l, n, r, i, a, b = 0, g = !1, c = !1, p = !0;
  if (typeof t != "function")
    throw new TypeError(ve);
  e = H(e) || 0, M(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Ie(H(o.maxWait) || 0, e) : n, p = "trailing" in o ? !!o.trailing : p);
  function d(_) {
    var E = s, S = l;
    return s = l = void 0, b = _, r = t.apply(S, E), r;
  }
  function w(_) {
    return b = _, i = setTimeout(h, e), g ? d(_) : r;
  }
  function f(_) {
    var E = _ - a, S = _ - b, F = e - E;
    return c ? Re(F, n - S) : F;
  }
  function m(_) {
    var E = _ - a, S = _ - b;
    return a === void 0 || E >= e || E < 0 || c && S >= n;
  }
  function h() {
    var _ = N();
    if (m(_))
      return C(_);
    i = setTimeout(h, f(_));
  }
  function C(_) {
    return i = void 0, p && s ? d(_) : (s = l = void 0, r);
  }
  function v() {
    i !== void 0 && clearTimeout(i), b = 0, s = a = l = i = void 0;
  }
  function u() {
    return i === void 0 ? r : C(N());
  }
  function I() {
    var _ = N(), E = m(_);
    if (s = arguments, l = this, a = _, E) {
      if (i === void 0)
        return w(a);
      if (c)
        return clearTimeout(i), i = setTimeout(h, e), d(a);
    }
    return i === void 0 && (i = setTimeout(h, e)), r;
  }
  return I.cancel = v, I.flush = u, I;
}
var Z = {
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
var ke = y, Oe = Symbol.for("react.element"), Te = Symbol.for("react.fragment"), Pe = Object.prototype.hasOwnProperty, je = ke.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Le = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function $(t, e, o) {
  var s, l = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), e.key !== void 0 && (n = "" + e.key), e.ref !== void 0 && (r = e.ref);
  for (s in e) Pe.call(e, s) && !Le.hasOwnProperty(s) && (l[s] = e[s]);
  if (t && t.defaultProps) for (s in e = t.defaultProps, e) l[s] === void 0 && (l[s] = e[s]);
  return {
    $$typeof: Oe,
    type: t,
    key: n,
    ref: r,
    props: l,
    _owner: je.current
  };
}
L.Fragment = Te;
L.jsx = $;
L.jsxs = $;
Z.exports = L;
var x = Z.exports;
const {
  SvelteComponent: Ne,
  assign: z,
  binding_callbacks: G,
  check_outros: Ae,
  children: ee,
  claim_element: te,
  claim_space: We,
  component_subscribe: q,
  compute_slots: Me,
  create_slot: Be,
  detach: R,
  element: ne,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: De,
  get_slot_changes: Fe,
  group_outros: Ue,
  init: He,
  insert_hydration: O,
  safe_not_equal: ze,
  set_custom_element_data: re,
  space: Ge,
  transition_in: T,
  transition_out: B,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ve,
  getContext: Je,
  onDestroy: Xe,
  setContext: Ye
} = window.__gradio__svelte__internal;
function X(t) {
  let e, o;
  const s = (
    /*#slots*/
    t[7].default
  ), l = Be(
    s,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = ne("svelte-slot"), l && l.c(), this.h();
    },
    l(n) {
      e = te(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ee(e);
      l && l.l(r), r.forEach(R), this.h();
    },
    h() {
      re(e, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, e, r), l && l.m(e, null), t[9](e), o = !0;
    },
    p(n, r) {
      l && l.p && (!o || r & /*$$scope*/
      64) && qe(
        l,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? Fe(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : De(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (T(l, n), o = !0);
    },
    o(n) {
      B(l, n), o = !1;
    },
    d(n) {
      n && R(e), l && l.d(n), t[9](null);
    }
  };
}
function Ke(t) {
  let e, o, s, l, n = (
    /*$$slots*/
    t[4].default && X(t)
  );
  return {
    c() {
      e = ne("react-portal-target"), o = Ge(), n && n.c(), s = V(), this.h();
    },
    l(r) {
      e = te(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ee(e).forEach(R), o = We(r), n && n.l(r), s = V(), this.h();
    },
    h() {
      re(e, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      O(r, e, i), t[8](e), O(r, o, i), n && n.m(r, i), O(r, s, i), l = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && T(n, 1)) : (n = X(r), n.c(), T(n, 1), n.m(s.parentNode, s)) : n && (Ue(), B(n, 1, 1, () => {
        n = null;
      }), Ae());
    },
    i(r) {
      l || (T(n), l = !0);
    },
    o(r) {
      B(n), l = !1;
    },
    d(r) {
      r && (R(e), R(o), R(s)), t[8](null), n && n.d(r);
    }
  };
}
function Y(t) {
  const {
    svelteInit: e,
    ...o
  } = t;
  return o;
}
function Qe(t, e, o) {
  let s, l, {
    $$slots: n = {},
    $$scope: r
  } = e;
  const i = Me(n);
  let {
    svelteInit: a
  } = e;
  const b = k(Y(e)), g = k();
  q(t, g, (u) => o(0, s = u));
  const c = k();
  q(t, c, (u) => o(1, l = u));
  const p = [], d = Je("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: m
  } = fe() || {}, h = a({
    parent: d,
    props: b,
    target: g,
    slot: c,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: m,
    onDestroy(u) {
      p.push(u);
    }
  });
  Ye("$$ms-gr-react-wrapper", h), Ve(() => {
    b.set(Y(e));
  }), Xe(() => {
    p.forEach((u) => u());
  });
  function C(u) {
    G[u ? "unshift" : "push"](() => {
      s = u, g.set(s);
    });
  }
  function v(u) {
    G[u ? "unshift" : "push"](() => {
      l = u, c.set(l);
    });
  }
  return t.$$set = (u) => {
    o(17, e = z(z({}, e), J(u))), "svelteInit" in u && o(5, a = u.svelteInit), "$$scope" in u && o(6, r = u.$$scope);
  }, e = J(e), [s, l, g, c, i, a, r, n, C, v];
}
class Ze extends Ne {
  constructor(e) {
    super(), He(this, e, Qe, Ke, ze, {
      svelteInit: 5
    });
  }
}
const K = window.ms_globals.rerender, A = window.ms_globals.tree;
function $e(t, e = {}) {
  function o(s) {
    const l = k(), n = new Ze({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: l,
            reactComponent: t,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: e.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? A;
          return a.nodes = [...a.nodes, i], K({
            createPortal: W,
            node: A
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((b) => b.svelteInstance !== l), K({
              createPortal: W,
              node: A
            });
          }), i;
        },
        ...s.props
      }
    });
    return l.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const et = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function tt(t) {
  return t ? Object.keys(t).reduce((e, o) => {
    const s = t[o];
    return e[o] = nt(o, s), e;
  }, {}) : {};
}
function nt(t, e) {
  return typeof e == "number" && !et.includes(t) ? e + "px" : e;
}
function D(t) {
  const e = [], o = t.cloneNode(!1);
  if (t._reactElement) {
    const l = y.Children.toArray(t._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = D(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return l.originalChildren = t._reactElement.props.children, e.push(W(y.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: l
    }), o)), {
      clonedElement: o,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((l) => {
    t.getEventListeners(l).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      o.addEventListener(i, r, a);
    });
  });
  const s = Array.from(t.childNodes);
  for (let l = 0; l < s.length; l++) {
    const n = s[l];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = D(n);
      e.push(...i), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: e
  };
}
function rt(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const j = se(({
  slot: t,
  clone: e,
  className: o,
  style: s,
  observeAttributes: l
}, n) => {
  const r = oe(), [i, a] = ie([]), {
    forceClone: b
  } = me(), g = b ? !0 : e;
  return ce(() => {
    var w;
    if (!r.current || !t)
      return;
    let c = t;
    function p() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), rt(n, f), o && f.classList.add(...o.split(" ")), s) {
        const m = tt(s);
        Object.keys(m).forEach((h) => {
          f.style[h] = m[h];
        });
      }
    }
    let d = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var v, u, I;
        (v = r.current) != null && v.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: h,
          clonedElement: C
        } = D(t);
        c = C, a(h), c.style.display = "contents", p(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const m = Se(() => {
        f(), d == null || d.disconnect(), d == null || d.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: l
        });
      }, 50);
      d = new window.MutationObserver(m), d.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", p(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var f, m;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((m = r.current) == null || m.removeChild(c)), d == null || d.disconnect();
    };
  }, [t, g, o, s, n, l]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function le(t, e, o) {
  const s = t.filter(Boolean);
  if (s.length !== 0)
    return s.map((l, n) => {
      var b;
      if (typeof l != "object")
        return e != null && e.fallback ? e.fallback(l) : l;
      const r = {
        ...l.props,
        key: ((b = l.props) == null ? void 0 : b.key) ?? (o ? `${o}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(l.slots).forEach((g) => {
        if (!l.slots[g] || !(l.slots[g] instanceof Element) && !l.slots[g].el)
          return;
        const c = g.split(".");
        c.forEach((h, C) => {
          i[h] || (i[h] = {}), C !== c.length - 1 && (i = r[h]);
        });
        const p = l.slots[g];
        let d, w, f = (e == null ? void 0 : e.clone) ?? !1, m = e == null ? void 0 : e.forceClone;
        p instanceof Element ? d = p : (d = p.el, w = p.callback, f = p.clone ?? f, m = p.forceClone ?? m), m = m ?? !!w, i[c[c.length - 1]] = d ? w ? (...h) => (w(c[c.length - 1], h), /* @__PURE__ */ x.jsx(P, {
          params: h,
          forceClone: m,
          children: /* @__PURE__ */ x.jsx(j, {
            slot: d,
            clone: f
          })
        })) : /* @__PURE__ */ x.jsx(P, {
          forceClone: m,
          children: /* @__PURE__ */ x.jsx(j, {
            slot: d,
            clone: f
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = (e == null ? void 0 : e.children) || "children";
      return l[a] ? r[a] = le(l[a], e, `${n}`) : e != null && e.children && (r[a] = void 0, Reflect.deleteProperty(r, a)), r;
    });
}
function Q(t, e) {
  return t ? /* @__PURE__ */ x.jsx(j, {
    slot: t,
    clone: e == null ? void 0 : e.clone
  }) : null;
}
function lt({
  key: t,
  slots: e,
  targets: o
}, s) {
  return e[t] ? (...l) => o ? o.map((n, r) => /* @__PURE__ */ x.jsx(P, {
    params: l,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: Q(n, {
      clone: !0,
      ...s
    })
  }, r)) : /* @__PURE__ */ x.jsx(P, {
    params: l,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: Q(e[t], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const {
  useItems: st,
  withItemsContextProvider: ot,
  ItemHandler: ct
} = he("antd-breadcrumb-items"), at = $e(ot(["default", "items"], ({
  slots: t,
  items: e,
  setSlotParams: o,
  children: s,
  ...l
}) => {
  const {
    items: n
  } = st(), r = n.items.length ? n.items : n.default;
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: s
    }), /* @__PURE__ */ x.jsx(_e, {
      ...l,
      itemRender: t.itemRender ? lt({
        setSlotParams: o,
        slots: t,
        key: "itemRender"
      }, {
        clone: !0
      }) : l.itemRender,
      items: ae(() => e || le(r, {
        // clone: true,
      }), [e, r]),
      separator: t.separator ? /* @__PURE__ */ x.jsx(j, {
        slot: t.separator,
        clone: !0
      }) : l.separator
    })]
  });
}));
export {
  at as Breadcrumb,
  at as default
};
