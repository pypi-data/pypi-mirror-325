import { i as de, a as W, r as ue, g as fe, w as k } from "./Index-BCRTocga.js";
const I = window.ms_globals.React, oe = window.ms_globals.React.forwardRef, se = window.ms_globals.React.useRef, ie = window.ms_globals.React.useState, ce = window.ms_globals.React.useEffect, ae = window.ms_globals.React.useMemo, M = window.ms_globals.ReactDOM.createPortal, me = window.ms_globals.internalContext.useContextPropsContext, T = window.ms_globals.internalContext.ContextPropsProvider, _e = window.ms_globals.antd.Menu, he = window.ms_globals.createItemsContext.createItemsContext;
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
var H = NaN, we = /^[-+]0x[0-9a-f]+$/i, ve = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, Ie = parseInt;
function z(t) {
  if (typeof t == "number")
    return t;
  if (de(t))
    return H;
  if (W(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = W(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = xe(t);
  var s = ve.test(t);
  return s || Ee.test(t) ? Ie(t.slice(2), s ? 2 : 8) : we.test(t) ? H : +t;
}
var N = function() {
  return ue.Date.now();
}, ye = "Expected a function", Ce = Math.max, Re = Math.min;
function Se(t, e, s) {
  var o, l, n, r, i, a, g = 0, m = !1, c = !1, b = !0;
  if (typeof t != "function")
    throw new TypeError(ye);
  e = z(e) || 0, W(s) && (m = !!s.leading, c = "maxWait" in s, n = c ? Ce(z(s.maxWait) || 0, e) : n, b = "trailing" in s ? !!s.trailing : b);
  function u(h) {
    var E = o, S = l;
    return o = l = void 0, g = h, r = t.apply(S, E), r;
  }
  function w(h) {
    return g = h, i = setTimeout(p, e), m ? u(h) : r;
  }
  function f(h) {
    var E = h - a, S = h - g, B = e - E;
    return c ? Re(B, n - S) : B;
  }
  function _(h) {
    var E = h - a, S = h - g;
    return a === void 0 || E >= e || E < 0 || c && S >= n;
  }
  function p() {
    var h = N();
    if (_(h))
      return v(h);
    i = setTimeout(p, f(h));
  }
  function v(h) {
    return i = void 0, b && o ? u(h) : (o = l = void 0, r);
  }
  function y() {
    i !== void 0 && clearTimeout(i), g = 0, o = a = l = i = void 0;
  }
  function d() {
    return i === void 0 ? r : v(N());
  }
  function C() {
    var h = N(), E = _(h);
    if (o = arguments, l = this, a = h, E) {
      if (i === void 0)
        return w(a);
      if (c)
        return clearTimeout(i), i = setTimeout(p, e), u(a);
    }
    return i === void 0 && (i = setTimeout(p, e)), r;
  }
  return C.cancel = y, C.flush = d, C;
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
var ke = I, Oe = Symbol.for("react.element"), Pe = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, je = ke.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Le = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function $(t, e, s) {
  var o, l = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), e.key !== void 0 && (n = "" + e.key), e.ref !== void 0 && (r = e.ref);
  for (o in e) Te.call(e, o) && !Le.hasOwnProperty(o) && (l[o] = e[o]);
  if (t && t.defaultProps) for (o in e = t.defaultProps, e) l[o] === void 0 && (l[o] = e[o]);
  return {
    $$typeof: Oe,
    type: t,
    key: n,
    ref: r,
    props: l,
    _owner: je.current
  };
}
L.Fragment = Pe;
L.jsx = $;
L.jsxs = $;
Z.exports = L;
var x = Z.exports;
const {
  SvelteComponent: Ne,
  assign: D,
  binding_callbacks: G,
  check_outros: Ae,
  children: ee,
  claim_element: te,
  claim_space: Me,
  component_subscribe: q,
  compute_slots: We,
  create_slot: Fe,
  detach: R,
  element: ne,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: Ue,
  get_slot_changes: Be,
  group_outros: He,
  init: ze,
  insert_hydration: O,
  safe_not_equal: De,
  set_custom_element_data: re,
  space: Ge,
  transition_in: P,
  transition_out: F,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ve,
  getContext: Je,
  onDestroy: Xe,
  setContext: Ye
} = window.__gradio__svelte__internal;
function X(t) {
  let e, s;
  const o = (
    /*#slots*/
    t[7].default
  ), l = Fe(
    o,
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
      O(n, e, r), l && l.m(e, null), t[9](e), s = !0;
    },
    p(n, r) {
      l && l.p && (!s || r & /*$$scope*/
      64) && qe(
        l,
        o,
        n,
        /*$$scope*/
        n[6],
        s ? Be(
          o,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ue(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (P(l, n), s = !0);
    },
    o(n) {
      F(l, n), s = !1;
    },
    d(n) {
      n && R(e), l && l.d(n), t[9](null);
    }
  };
}
function Ke(t) {
  let e, s, o, l, n = (
    /*$$slots*/
    t[4].default && X(t)
  );
  return {
    c() {
      e = ne("react-portal-target"), s = Ge(), n && n.c(), o = V(), this.h();
    },
    l(r) {
      e = te(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ee(e).forEach(R), s = Me(r), n && n.l(r), o = V(), this.h();
    },
    h() {
      re(e, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      O(r, e, i), t[8](e), O(r, s, i), n && n.m(r, i), O(r, o, i), l = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && P(n, 1)) : (n = X(r), n.c(), P(n, 1), n.m(o.parentNode, o)) : n && (He(), F(n, 1, 1, () => {
        n = null;
      }), Ae());
    },
    i(r) {
      l || (P(n), l = !0);
    },
    o(r) {
      F(n), l = !1;
    },
    d(r) {
      r && (R(e), R(s), R(o)), t[8](null), n && n.d(r);
    }
  };
}
function Y(t) {
  const {
    svelteInit: e,
    ...s
  } = t;
  return s;
}
function Qe(t, e, s) {
  let o, l, {
    $$slots: n = {},
    $$scope: r
  } = e;
  const i = We(n);
  let {
    svelteInit: a
  } = e;
  const g = k(Y(e)), m = k();
  q(t, m, (d) => s(0, o = d));
  const c = k();
  q(t, c, (d) => s(1, l = d));
  const b = [], u = Je("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _
  } = fe() || {}, p = a({
    parent: u,
    props: g,
    target: m,
    slot: c,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(d) {
      b.push(d);
    }
  });
  Ye("$$ms-gr-react-wrapper", p), Ve(() => {
    g.set(Y(e));
  }), Xe(() => {
    b.forEach((d) => d());
  });
  function v(d) {
    G[d ? "unshift" : "push"](() => {
      o = d, m.set(o);
    });
  }
  function y(d) {
    G[d ? "unshift" : "push"](() => {
      l = d, c.set(l);
    });
  }
  return t.$$set = (d) => {
    s(17, e = D(D({}, e), J(d))), "svelteInit" in d && s(5, a = d.svelteInit), "$$scope" in d && s(6, r = d.$$scope);
  }, e = J(e), [o, l, m, c, i, a, r, n, v, y];
}
class Ze extends Ne {
  constructor(e) {
    super(), ze(this, e, Qe, Ke, De, {
      svelteInit: 5
    });
  }
}
const K = window.ms_globals.rerender, A = window.ms_globals.tree;
function $e(t, e = {}) {
  function s(o) {
    const l = k(), n = new Ze({
      ...o,
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
            createPortal: M,
            node: A
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((g) => g.svelteInstance !== l), K({
              createPortal: M,
              node: A
            });
          }), i;
        },
        ...o.props
      }
    });
    return l.set(n), n;
  }
  return new Promise((o) => {
    window.ms_globals.initializePromise.then(() => {
      o(s);
    });
  });
}
const et = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function tt(t) {
  return t ? Object.keys(t).reduce((e, s) => {
    const o = t[s];
    return e[s] = nt(s, o), e;
  }, {}) : {};
}
function nt(t, e) {
  return typeof e == "number" && !et.includes(t) ? e + "px" : e;
}
function U(t) {
  const e = [], s = t.cloneNode(!1);
  if (t._reactElement) {
    const l = I.Children.toArray(t._reactElement.props.children).map((n) => {
      if (I.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = U(n.props.el);
        return I.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...I.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return l.originalChildren = t._reactElement.props.children, e.push(M(I.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: l
    }), s)), {
      clonedElement: s,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((l) => {
    t.getEventListeners(l).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      s.addEventListener(i, r, a);
    });
  });
  const o = Array.from(t.childNodes);
  for (let l = 0; l < o.length; l++) {
    const n = o[l];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = U(n);
      e.push(...i), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: e
  };
}
function rt(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const j = oe(({
  slot: t,
  clone: e,
  className: s,
  style: o,
  observeAttributes: l
}, n) => {
  const r = se(), [i, a] = ie([]), {
    forceClone: g
  } = me(), m = g ? !0 : e;
  return ce(() => {
    var w;
    if (!r.current || !t)
      return;
    let c = t;
    function b() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), rt(n, f), s && f.classList.add(...s.split(" ")), o) {
        const _ = tt(o);
        Object.keys(_).forEach((p) => {
          f.style[p] = _[p];
        });
      }
    }
    let u = null;
    if (m && window.MutationObserver) {
      let f = function() {
        var y, d, C;
        (y = r.current) != null && y.contains(c) && ((d = r.current) == null || d.removeChild(c));
        const {
          portals: p,
          clonedElement: v
        } = U(t);
        c = v, a(p), c.style.display = "contents", b(), (C = r.current) == null || C.appendChild(c);
      };
      f();
      const _ = Se(() => {
        f(), u == null || u.disconnect(), u == null || u.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: l
        });
      }, 50);
      u = new window.MutationObserver(_), u.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", b(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var f, _;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((_ = r.current) == null || _.removeChild(c)), u == null || u.disconnect();
    };
  }, [t, m, s, o, n, l]), I.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function lt(t) {
  return Object.keys(t).reduce((e, s) => (t[s] !== void 0 && (e[s] = t[s]), e), {});
}
function le(t, e, s) {
  const o = t.filter(Boolean);
  if (o.length !== 0)
    return o.map((l, n) => {
      var g;
      if (typeof l != "object")
        return e != null && e.fallback ? e.fallback(l) : l;
      const r = {
        ...l.props,
        key: ((g = l.props) == null ? void 0 : g.key) ?? (s ? `${s}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(l.slots).forEach((m) => {
        if (!l.slots[m] || !(l.slots[m] instanceof Element) && !l.slots[m].el)
          return;
        const c = m.split(".");
        c.forEach((p, v) => {
          i[p] || (i[p] = {}), v !== c.length - 1 && (i = r[p]);
        });
        const b = l.slots[m];
        let u, w, f = (e == null ? void 0 : e.clone) ?? !1, _ = e == null ? void 0 : e.forceClone;
        b instanceof Element ? u = b : (u = b.el, w = b.callback, f = b.clone ?? f, _ = b.forceClone ?? _), _ = _ ?? !!w, i[c[c.length - 1]] = u ? w ? (...p) => (w(c[c.length - 1], p), /* @__PURE__ */ x.jsx(T, {
          params: p,
          forceClone: _,
          children: /* @__PURE__ */ x.jsx(j, {
            slot: u,
            clone: f
          })
        })) : /* @__PURE__ */ x.jsx(T, {
          forceClone: _,
          children: /* @__PURE__ */ x.jsx(j, {
            slot: u,
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
function ot({
  key: t,
  slots: e,
  targets: s
}, o) {
  return e[t] ? (...l) => s ? s.map((n, r) => /* @__PURE__ */ x.jsx(T, {
    params: l,
    forceClone: (o == null ? void 0 : o.forceClone) ?? !0,
    children: Q(n, {
      clone: !0,
      ...o
    })
  }, r)) : /* @__PURE__ */ x.jsx(T, {
    params: l,
    forceClone: (o == null ? void 0 : o.forceClone) ?? !0,
    children: Q(e[t], {
      clone: !0,
      ...o
    })
  }) : void 0;
}
const {
  useItems: st,
  withItemsContextProvider: it,
  ItemHandler: at
} = he("antd-menu-items"), dt = $e(it(["default", "items"], ({
  slots: t,
  items: e,
  children: s,
  onOpenChange: o,
  onSelect: l,
  onDeselect: n,
  setSlotParams: r,
  ...i
}) => {
  const {
    items: a
  } = st(), g = a.items.length > 0 ? a.items : a.default;
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: s
    }), /* @__PURE__ */ x.jsx(_e, {
      ...lt(i),
      onOpenChange: (m) => {
        o == null || o(m);
      },
      onSelect: (m) => {
        l == null || l(m);
      },
      onDeselect: (m) => {
        n == null || n(m);
      },
      items: ae(() => e || le(g, {
        clone: !0
      }), [e, g]),
      expandIcon: t.expandIcon ? ot({
        key: "expandIcon",
        slots: t,
        setSlotParams: r
      }, {
        clone: !0
      }) : i.expandIcon,
      overflowedIndicator: t.overflowedIndicator ? /* @__PURE__ */ x.jsx(j, {
        slot: t.overflowedIndicator
      }) : i.overflowedIndicator
    })]
  });
}));
export {
  dt as Menu,
  dt as default
};
